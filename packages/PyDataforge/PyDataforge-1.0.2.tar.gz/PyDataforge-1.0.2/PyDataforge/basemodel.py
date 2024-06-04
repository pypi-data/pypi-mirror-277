import torch
from torch import nn


class Autoencoder(nn.Module):

    def __init__(self, dimension):
        super(Autoencoder, self).__init__()
        n_channels_base = 4
        self.encoder = nn.Sequential(
            nn.Conv1d(in_channels=1, out_channels=n_channels_base, kernel_size=dimension-6, stride=1,
                      padding=0, dilation=1,
                      groups=1, bias=True, padding_mode='zeros'),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv1d(in_channels=n_channels_base, out_channels=2 * n_channels_base, kernel_size=3, stride=1,
                      padding=0, dilation=1,
                      groups=1, bias=True, padding_mode='zeros'),
            nn.BatchNorm1d(n_channels_base * 2),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv1d(in_channels=n_channels_base*2, out_channels=3 * n_channels_base, kernel_size=3, stride=1,
                      padding=0, dilation=1,
                      groups=1, bias=True, padding_mode='zeros'),
            nn.BatchNorm1d(n_channels_base * 3),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv1d(in_channels=n_channels_base * 3, out_channels=n_channels_base * 4, kernel_size=3, stride=1,
                      padding=0, dilation=1,
                      groups=1, bias=True, padding_mode='zeros'),
            nn.Tanh(),
        )

        self.decoder = nn.Sequential(
            nn.ConvTranspose1d(in_channels=n_channels_base * 4, out_channels=3 * n_channels_base, kernel_size=3,
                               stride=1, padding=0, dilation=1,
                               groups=1, bias=True, padding_mode='zeros'),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose1d(in_channels=3 * n_channels_base, out_channels=2*n_channels_base, kernel_size=3,
                               stride=1, padding=0, dilation=1,
                               groups=1, bias=True, padding_mode='zeros'),
            nn.BatchNorm1d(n_channels_base*2),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose1d(in_channels=2 * n_channels_base, out_channels=n_channels_base, kernel_size=3,
                               stride=1, padding=0, dilation=1,
                               groups=1, bias=True, padding_mode='zeros'),
            nn.BatchNorm1d(n_channels_base),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose1d(in_channels=n_channels_base, out_channels=1, kernel_size=dimension-6, stride=1,
                               padding=0, dilation=1,
                               groups=1, bias=True, padding_mode='zeros'),
            nn.Sigmoid(),
        )

    def forward(self, x):
        x = self.encoder(x.view(-1, 1, x.shape[1]))
        x = self.decoder(x)
        return torch.squeeze(x, dim=1)


class Encoder(nn.Module):

    def __init__(self, dimension):
        super(Encoder, self).__init__()
        n_channels_base = 4

        self.main = nn.Sequential(
            nn.Conv1d(in_channels=1, out_channels=n_channels_base, kernel_size=dimension-6, stride=1,
                      padding=0, dilation=1,
                      groups=1, bias=True, padding_mode='zeros'),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv1d(in_channels=n_channels_base, out_channels=2 * n_channels_base, kernel_size=3, stride=1,
                      padding=0, dilation=1,
                      groups=1, bias=True, padding_mode='zeros'),
            nn.BatchNorm1d(n_channels_base * 2),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv1d(in_channels=n_channels_base * 2, out_channels=4 * n_channels_base, kernel_size=3, stride=1,
                      padding=0, dilation=1,
                      groups=1, bias=True, padding_mode='zeros'),
            nn.BatchNorm1d(n_channels_base * 4),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv1d(in_channels=n_channels_base * 4, out_channels=n_channels_base * 16, kernel_size=3, stride=1,
                      padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros'),
            nn.Tanh(),
        )

    def forward(self, x):
        x = self.main(x.view(-1, 1, x.shape[1]))
        return torch.squeeze(x, dim=2)


class Generator(nn.Module):
    def __init__(self, latent_dim):
        super(Generator, self).__init__()
        ngf = 4
        ngf = 4
        self.main = nn.Sequential(
            nn.ConvTranspose1d(latent_dim, ngf * 8, 5, 1, 0),
            nn.BatchNorm1d(ngf * 8, eps=0.0001, momentum=0.01),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose1d(ngf * 8, ngf * 4, 5, 1, 0),
            nn.BatchNorm1d(ngf * 4, eps=0.0001, momentum=0.01),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose1d(ngf * 4, ngf*2, 4, 1, 0),
            nn.BatchNorm1d(ngf*2, eps=0.0001, momentum=0.01),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose1d(ngf*2, ngf, 3, 1, 0),
            nn.BatchNorm1d(ngf, eps=0.0001, momentum=0.01),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose1d(ngf, 1, 3, 1, 0),
            nn.Tanh(),
        )

    def forward(self, x):
        x = x.view(-1, x.shape[1], 1)
        out = self.main(x)
        return torch.squeeze(out, dim=1)


class Discriminator(nn.Module):

    def __init__(self, dimension):
        super(Discriminator, self).__init__()
        ndf = 4
        self.conv1 = nn.Sequential(
            nn.Conv1d(1, ndf, kernel_size=dimension//2+3, stride=dimension//2, padding=0),
            nn.BatchNorm1d(ndf),
            nn.LeakyReLU(0.2, inplace=True),
        )
        self.conv2 = nn.Sequential(
            nn.Conv1d(1, 2 * ndf, 15, 3, 0),
            nn.BatchNorm1d(2 * ndf),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv1d(ndf * 2, ndf * 4, 14, 4, 0),
            nn.LeakyReLU(0.2, inplace=True),
        )
        self.conv4 = nn.Sequential(
            # state size. (ndf*8) x 4 x 4
            nn.Conv1d(1, ndf * 2, 7, 2, 0),
            nn.BatchNorm1d(ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv1d(ndf * 2, 1, 6, 2, 0),
            nn.Sigmoid()
        )

    def forward(self, x, z):
        out_x = self.conv1(x.view(-1, 1, x.shape[1]))
        out_x = torch.squeeze(out_x, dim=2)

        out_z = self.conv2(z.view(-1, 1, z.shape[1]))
        out_z = torch.squeeze(out_z, dim=2)

        out = torch.cat([out_x, out_z], dim=1)
        out = self.conv4(out.view(-1, 1, out.shape[1]))

        return torch.squeeze(out, dim=2)