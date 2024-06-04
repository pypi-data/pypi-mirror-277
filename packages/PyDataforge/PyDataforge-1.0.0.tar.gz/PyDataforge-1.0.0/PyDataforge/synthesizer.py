import numpy as np
import random
import os
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import DataLoader
from torch.autograd import Variable
import torch.backends.cudnn as cudnn
import torch.nn as nn
import torch
from ForgeCore.evaluation import mse_loss, distance, mmd_test, mmd
from ForgeCore.basemodel import Discriminator, Generator, Autoencoder, Encoder


class Dataset:
    def __init__(self, data, transform=None):
        self.transform = transform
        self.data = data
        self.sampleSize = data.shape[0]
        self.featureSize = data.shape[1]

    def return_data(self):
        return self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        sample = self.data[idx]
        if self.transform:
            pass
        return torch.from_numpy(sample)


def weights_init(m):
    """
    权重初始化函数

    参数:
    - m (nn.Module): 要初始化权重的模块

    该函数用于对神经网络模块进行权重初始化。
    如果模块是卷积层(Conv)，则使用正态分布初始化权重和偏置，标准差分别为0.02和0.01。
    如果模块是批归一化层(BatchNorm)，则使用正态分布初始化权重和常数初始化偏置，均值和标准差分别为1和0.2。
    如果模块是全连接层(Linear)，则使用Xavier均匀分布初始化权重，偏置初始化为0.01。
    """
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        nn.init.normal_(m.weight.data, 0.0, 0.02)
        m.bias.data.fill_(0.01)
    elif classname.find('BatchNorm') != -1:
        nn.init.normal_(m.weight.data, 1.0, 0.2)
        nn.init.constant_(m.bias.data, 0)
    elif type(m) == nn.Linear:
        nn.init.xavier_uniform_(m.weight)
        m.bias.data.fill_(0.01)


def print_table(title, data):
    print(title + ":")
    print("-" * 50)
    for key, value in data.items():
        print(f"{key:<20} {value}")
    print("-" * 50)


class Synthesizer_CNN:

    def __init__(self, expPATH, input_dim, batch_size=64, sample_interval=10, lr=0.0002, cuda=False,
                 multiple_gpu=False,
                 num_gpu=2):
        """
        初始化函数

        参数:
        - expPATH (str): 实验结果保存路径
        - input_dim (int): 输入数据维度
        - batch_size (int): 每批次样本数，默认为64
        - sample_interval (int): 打印训练信息的间隔，以批次为单位，默认为10
        - lr (float): 学习率，默认为0.0002
        - cuda (bool): 是否使用CUDA，默认为False
        - multiple_gpu (bool): 是否使用多个GPU，默认为False
        - num_gpu (int): multiple_gpu为True时，使用的GPU数量，默认为2
        """

        self.expPATH = expPATH

        # PyTorch随机种子
        random.seed(random.randint(1, 10000))
        torch.manual_seed(random.randint(1, 10000))
        np.random.seed(random.randint(1, 10000))
        cudnn.benchmark = True

        # 激活CUDA
        self.device = torch.device("cuda:0" if cuda else "cpu")

        # 噪声空间维度
        self.latent_dim = 64
        # 初始化生成器和判别器
        self.discriminatorModel = Discriminator(input_dim)
        self.generatorModel = Generator(self.latent_dim)
        self.autoencoderModel = Autoencoder(input_dim)
        self.autoencoderDecoder = self.autoencoderModel.decoder
        self.EncoderModel = Encoder(input_dim)

        # 定义CUDA张量
        self.Tensor = torch.FloatTensor
        self.one = torch.FloatTensor([1])
        self.mone = self.one * -1

        # 其他设置
        self.batch_size = batch_size
        self.sample_interval = sample_interval
        self.discretize_columns = []

        if torch.cuda.device_count() >= 1 and multiple_gpu:
            self.generatorModel = nn.DataParallel(self.generatorModel, list(range(num_gpu)))
            self.discriminatorModel = nn.DataParallel(self.discriminatorModel, list(range(num_gpu)))
            self.autoencoderModel = nn.DataParallel(self.autoencoderModel, list(range(num_gpu)))
            self.autoencoderDecoder = nn.DataParallel(self.autoencoderDecoder, list(range(num_gpu)))
            self.EncoderModel = nn.DataParallel(self.EncoderModel, list(range(num_gpu)))

        if cuda:
            self.generatorModel.cuda()
            self.discriminatorModel.cuda()
            self.autoencoderModel.cuda()
            self.autoencoderDecoder.cuda()
            self.EncoderModel.cuda()
            self.one, self.mone = self.one.cuda(), self.mone.cuda()
            self.Tensor = torch.cuda.FloatTensor

        # 损失函数
        self.criterion = nn.BCELoss()

        # 权重初始化
        self.generatorModel.apply(weights_init)
        self.discriminatorModel.apply(weights_init)
        self.autoencoderModel.apply(weights_init)
        self.EncoderModel.apply(weights_init)

        # 优化器
        b1 = 0.5  # adam: 梯度的第一阶矩衰减率
        b2 = 0.999  # adam: 梯度的第二阶矩衰减率
        weight_decay = 0.0  # 优化器的权重衰减

        self.optimizer_G = torch.optim.Adam([
            {'params': self.generatorModel.parameters()},
            {'params': self.autoencoderDecoder.parameters(), 'lr': 1e-4}
        ], lr=lr, betas=(b1, b2), weight_decay=weight_decay)

        self.optimizer_D = torch.optim.Adam(
            params=self.discriminatorModel.parameters(),
            lr=lr,
            betas=(b1, b2),
            weight_decay=weight_decay,
        )

        self.optimizer_E = torch.optim.Adam(
            params=self.EncoderModel.parameters(),
            lr=0.001,
            betas=(b1, b2),
            weight_decay=weight_decay,
        )

        self.optimizer_A = torch.optim.Adam(
            params=self.autoencoderModel.parameters(),
            lr=lr,
            betas=(b1, b2),
            weight_decay=weight_decay,
        )

    def fit(self, trainData, discretize_columns, n_epochs_pretrain=50, n_epochs=100):
        """
        拟合函数

        参数:
        - trainData (DataFrame): 训练数据
        - discretize_columns (list): 二分类特征的列索引
        - n_epochs_pretrain (int): 预训练AutoEncoder的轮数，默认为50。
        - n_epochs (int): 训练GAN的轮数，默认为100。
        """
        self.discretize_columns = discretize_columns
        # 调整数据类型
        trainData = trainData.astype(np.float32)

        # 对数据进行归一化处理
        sc = MinMaxScaler()
        trainData = sc.fit_transform(trainData)

        # 创建数据集对象
        dataset_train_object = Dataset(data=trainData, transform=False)

        # 创建数据加载器
        dataloader_train = DataLoader(dataset_train_object, batch_size=self.batch_size,
                                      shuffle=True, num_workers=0, drop_last=True)

        # 预训练阶段
        for epoch_pre in range(n_epochs_pretrain):
            for i_batch, samples in enumerate(dataloader_train):
                real_samples = Variable(samples.type(self.Tensor))

                self.optimizer_A.zero_grad()

                micro_batch = real_samples

                recons_samples = self.autoencoderModel(micro_batch)
                a_loss = mse_loss(recons_samples, micro_batch, self.batch_size)
                a_loss.backward()
                self.optimizer_A.step()

                batches_done = epoch_pre * len(dataloader_train) + i_batch + 1

                if batches_done % self.sample_interval == 0:
                    print(
                        "[Epoch %d/%d of pretraining] [Batch %d/%d] [A loss: %.3f]"
                        % (epoch_pre + 1, n_epochs_pretrain, i_batch + 1, len(dataloader_train), a_loss.item())
                    )
        # 训练阶段
        gen_iterations = 0
        for epoch in range(0, n_epochs):
            for i_batch, samples in enumerate(dataloader_train):
                real_samples = Variable(samples.type(self.Tensor))

                valid = Variable(self.Tensor(samples.shape[0]).fill_(1.0), requires_grad=False)
                fake_truths = Variable(self.Tensor(samples.shape[0]).fill_(0.0), requires_grad=False)

                self.optimizer_D.zero_grad()

                micro_batch = real_samples

                for p in self.discriminatorModel.parameters():  # reset requires_grad
                    p.requires_grad = True

                z_real = self.EncoderModel(micro_batch)
                out_real = self.discriminatorModel(micro_batch, z_real.detach()).view(-1)
                real_loss = self.criterion(out_real, valid)

                z = torch.randn(samples.shape[0], self.latent_dim, device=self.device)

                fake = self.generatorModel(z)

                fake_decoded = torch.squeeze(self.autoencoderDecoder(fake.unsqueeze(dim=2)), dim=1)

                out_fake = self.discriminatorModel(fake_decoded.detach(), z).view(-1)
                fake_loss = self.criterion(out_fake, fake_truths)

                d_loss = (real_loss + fake_loss)

                d_loss.backward()
                self.optimizer_D.step()

                for p in self.discriminatorModel.parameters():  # reset requires_grad
                    p.requires_grad = False

                self.optimizer_G.zero_grad()

                z = torch.randn(samples.shape[0], self.latent_dim, device=self.device)

                fake = self.generatorModel(z)

                fake_decoded = torch.squeeze(self.autoencoderDecoder(fake.unsqueeze(dim=2)), dim=1)

                g_loss = self.criterion(self.discriminatorModel(fake_decoded, z).view(-1), valid)

                self.optimizer_E.zero_grad()
                z_real = self.EncoderModel(micro_batch)
                e_loss = self.criterion(self.discriminatorModel(micro_batch, z_real).view(-1), fake_truths)

                fake1 = self.generatorModel(z_real)
                fake_decoded1 = torch.squeeze(self.autoencoderDecoder(fake1.unsqueeze(dim=2)), dim=1)
                rec_loss = (mse_loss(fake_decoded, micro_batch, self.batch_size)) * 0.2

                Mxx = distance(micro_batch, micro_batch, False)
                Mxy = distance(micro_batch, fake_decoded, False)
                Myy = distance(fake_decoded, fake_decoded, False)
                sigma = 1

                Mxx1 = distance(micro_batch, micro_batch, False)
                Mxy1 = distance(micro_batch, fake_decoded1, False)
                Myy1 = distance(fake_decoded1, fake_decoded1, False)
                mmd_loss = mmd(Mxx, Mxy, Myy, sigma) + mmd(Mxx1, Mxy1, Myy1, sigma)

                loss = 7 * mmd_loss + e_loss + g_loss - rec_loss
                loss.backward()

                self.optimizer_E.step()
                self.optimizer_G.step()
                gen_iterations += 1
                batches_done = epoch * len(dataloader_train) + i_batch + 1
                if batches_done % self.sample_interval == 0:
                    print(
                        'TRAIN: [Epoch %d/%d] [Batch %d/%d] Loss_D: %.6f Loss_G: %.6f Loss_E: %.6f Loss_MMD: %.6f '
                        'Loss_REC: %.6f'
                        % (
                            epoch + 1, n_epochs, i_batch + 1, len(dataloader_train), d_loss.item(),
                            g_loss.item(),
                            e_loss.item(), mmd_loss.item(), rec_loss.item())
                    )
        torch.save({
            'epoch': n_epochs,
            'Generator_state_dict': self.generatorModel.state_dict(),
            'Discriminator_state_dict': self.discriminatorModel.state_dict(),
            'Autoencoder_state_dict': self.autoencoderModel.state_dict(),
            'Autoencoder_Decoder_state_dict': self.autoencoderDecoder.state_dict(),
            'Encoder_state_dict': self.EncoderModel.state_dict(),
            'optimizer_G_state_dict': self.optimizer_G.state_dict(),
            'optimizer_D_state_dict': self.optimizer_D.state_dict(),
            'optimizer_A_state_dict': self.optimizer_A.state_dict(),
            'optimizer_E_state_dict': self.optimizer_E.state_dict(),
        }, os.path.join(self.expPATH, "synthesizer.pth"))

    def generate(self, shape_x, shape_y):
        """
        生成函数

        参数:
        - shape_x (tuple): 生成数据样本的数量

        返回值:
        - gen_samples (numpy): 生成的数据
        """

        checkpoint = torch.load(os.path.join(self.expPATH, "synthesizer.pth"))

        self.generatorModel.load_state_dict(checkpoint['Generator_state_dict'])
        self.autoencoderModel.load_state_dict(checkpoint['Autoencoder_state_dict'])
        self.autoencoderDecoder.load_state_dict(checkpoint['Autoencoder_Decoder_state_dict'])
        self.EncoderModel.load_state_dict(checkpoint['Encoder_state_dict'])

        self.generatorModel.eval()
        self.autoencoderModel.eval()
        self.autoencoderDecoder.eval()
        self.EncoderModel.eval()

        num_fake_samples = shape_x*3
        gen_samples = np.zeros([shape_x*3, shape_y])
        n_batches = int(num_fake_samples / self.batch_size)

        for i in range(n_batches):
            z = torch.randn(self.batch_size, self.latent_dim, device=self.device)
            gen_samples_tensor = self.generatorModel(z)
            gen_samples_decoded = torch.squeeze(
                self.autoencoderDecoder(gen_samples_tensor.view(-1, gen_samples_tensor.shape[1], 1)))
            gen_samples[i * self.batch_size:(i + 1) * self.batch_size, :] = gen_samples_decoded.cpu().data.numpy()

            assert (gen_samples[i, :] != gen_samples[i, :]).any() == False

        gen_samples = np.delete(gen_samples, np.s_[(i + 1) * self.batch_size:], 0)

        # 对离散列进行离散化
        max_iterations = 5

        for col_index in self.discretize_columns:
            ratio = 0.5
            iteration = 0
            while iteration < max_iterations:
                iteration += 1
                # 复制一份原始数据
                original_gen_samples = np.copy(gen_samples)

                # 根据 ratio 对列进行离散化
                gen_samples[gen_samples[:, col_index] >= ratio, col_index] = 1
                gen_samples[gen_samples[:, col_index] < ratio, col_index] = 0
                gen_samples = gen_samples[0:shape_x]

                # 检查每列的值是否全为1或全为0
                if np.all(gen_samples[:, col_index] == 1):
                    ratio += 0.1
                    gen_samples = np.copy(original_gen_samples)
                elif np.all(gen_samples[:, col_index] == 0):
                    ratio -= 0.1
                    gen_samples = np.copy(original_gen_samples)
                # 否则，跳出循环
                else:
                    print("For col", col_index, ", Division ratio is ", ratio)
                    break

            if abs(ratio) <= 1e-4 or abs(ratio-1.0) <= 1e-4:
                print("The ratio may lead to error, please try running again!")

        gen_samples = gen_samples.astype(np.float32)
        return gen_samples

    def evaluate(self, origin_data, synthetic_data):
        real_samples = origin_data.astype(np.float32)
        sc = MinMaxScaler()
        real_samples = sc.fit_transform(real_samples)

        real_samples_mmd = torch.from_numpy(real_samples).float().to(self.device)
        gen_samples_mmd = torch.from_numpy(synthetic_data).float().to(self.device)

        real = real_samples_mmd[0:10000]
        fake = gen_samples_mmd[0:10000]
        Mxx = distance(real, real, False)
        Mxy = distance(real, fake, False)
        Myy = distance(fake, fake, False)
        sigma = 1
        mmd_value = mmd_test(Mxx, Mxy, Myy, sigma)

        loss = nn.MSELoss(reduction='sum')
        mse_value = loss(gen_samples_mmd, real_samples_mmd)

        table_data = {
            '分布相似度（MMD）': f'{mmd_value:.4f}',
            '脱敏效果（RMSE）': f'{torch.sqrt(mse_value):.4f}'
        }

        print_table("评估结果", table_data)
