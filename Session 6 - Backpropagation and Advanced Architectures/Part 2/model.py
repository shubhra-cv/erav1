
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary
from tqdm import tqdm

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, 3, bias=False) #input -? OUtput? RF2
        self.BN1=nn.BatchNorm2d(8)
        self.conv2 = nn.Conv2d(8, 16, 3, bias=False)
        self.BN2=nn.BatchNorm2d(16)
        self.conv3 = nn.Conv2d(16, 32, 3, bias=False)
        self.BN3=nn.BatchNorm2d(32)
        self.pool1 = nn.MaxPool2d(2, 2)

        self.conv4 = nn.Conv2d(32, 8, 3, bias=False) #input -? OUtput? RF2
        self.BN4=nn.BatchNorm2d(8)
        self.conv5 = nn.Conv2d(8, 16, 3, bias=False)
        self.BN5=nn.BatchNorm2d(16)
        self.conv6 = nn.Conv2d(16, 16, 3, bias=False) #4x4
        self.BN6=nn.BatchNorm2d(16)
        self.conv7 = nn.Conv2d(16, 16, 3, bias=False,padding=1)
        self.BN7=nn.BatchNorm2d(16)
        self.conv8 = nn.Conv2d(16, 10, 3, bias=False,padding=1)
        self.dropout=nn.Dropout(p=0.05)

        

        # self.conv9 = nn.Conv2d(512, 10, 1, bias=False)
        # self.conv7 = nn.Conv2d(1024, 10, 3, bias=False)

    def forward(self, x):
      x=self.conv1(x)
      x=self.BN1(x)
      x=self.dropout(x)
      x=F.relu(x)
      x=self.conv2(x)
      x=self.BN2(x)
      x=self.dropout(x)
      x=F.relu(x)
      x=self.pool1(x)
      ##########################
      x=self.conv3(x)
      x=self.BN3(x)
      x=self.dropout(x)
      x=F.relu(x)
      x=self.conv4(x)
      x=self.BN4(x)
      x=self.dropout(x)
      x=F.relu(x)
      ##########################
      x=self.conv5(x)
      x=self.BN5(x)
      x=self.dropout(x)
      x=F.relu(x)
      x=self.conv6(x)
      x=self.BN6(x)
      x=self.dropout(x)
      x=F.relu(x)
      x=self.conv7(x)
      x=self.BN7(x)
      x=self.dropout(x)
      x=F.relu(x)
      x=self.conv8(x)
      x=F.relu(x)
      # Global Average Pooling
      x = F.avg_pool2d(x, x.size()[2:])
      x = x.view(-1, 10)
      return F.log_softmax(x)
    

def model_summary(model,input_size=(1, 28, 28)):
    summary(model, input_size)

def train(model, device, train_loader, optimizer, epoch):
    model.train()
    pbar = tqdm(train_loader)
    for batch_idx, (data, target) in enumerate(pbar):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        pbar.set_description(desc= f'loss={loss.item()} batch_id={batch_idx}')


def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
            pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))