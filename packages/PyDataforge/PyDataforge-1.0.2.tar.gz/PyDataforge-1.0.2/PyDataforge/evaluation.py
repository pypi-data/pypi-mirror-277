import math
import torch.nn as nn
import torch


def mse_loss(x_output, y_target, batch_size):
    loss = nn.MSELoss(reduction='sum')
    l = loss(x_output, y_target) / batch_size
    return l


def distance(X, Y, sqrt):
    nX = X.size(0)
    nY = Y.size(0)
    if torch.cuda.is_available():
        X = X.view(nX, -1).cuda()
        Y = Y.view(nY, -1).cuda()
    else:
        X = X.view(nX, -1)
        Y = Y.view(nY, -1)
    X2 = (X * X).sum(1).reshape(nX, 1)
    Y2 = (Y * Y).sum(1).reshape(nY, 1)

    M = torch.zeros(nX, nY)
    M.copy_(X2.expand(nX, nY) + Y2.expand(nY, nX).transpose(0, 1) - 2 * torch.mm(X, Y.transpose(0, 1)))

    del X, X2, Y, Y2

    if sqrt:
        M = ((M + M.abs()) / 2).sqrt()

    return M


def mmd(Mxx, Mxy, Myy, sigma):
    scale = Mxx.mean()
    Mxx = torch.exp(-Mxx / (scale * 2 * sigma * sigma))
    Mxy = torch.exp(-Mxy / (scale * 2 * sigma * sigma))
    Myy = torch.exp(-Myy / (scale * 2 * sigma * sigma))
    a = Mxx.mean() + Myy.mean() - 2 * Mxy.mean()
    if a > 0:
        mmd = a.sqrt()
    else:
        mmd = 0
    return mmd


def mmd_test(Mxx, Mxy, Myy, sigma):
    scale = Mxx.mean()
    Mxx = torch.exp(-Mxx / (scale * 2 * sigma * sigma))
    Mxy = torch.exp(-Mxy / (scale * 2 * sigma * sigma))
    Myy = torch.exp(-Myy / (scale * 2 * sigma * sigma))
    a = Mxx.mean() + Myy.mean() - 2 * Mxy.mean()
    mmd = math.sqrt(max(a, 0))
    return mmd


