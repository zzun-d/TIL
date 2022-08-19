import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader

if torch.cuda.is_available():
    device = torch.device("cuda") 
else:
    device = torch.device("cpu")


def get_data_loaders(train_batch_size, val_batch_size):
    # fashion_mnist = torchvision.datasets.FashionMNIST(
    #     download=True, 
    #     train=True, 
    #     root=".").train_data.float()
    
    # data_transform = transforms.Compose([ # Compose : transforms 리스트 구성
    #     transforms.Resize((224, 224)), # Resize : 입력 이미지의 크기를 지정된 크기로 조정
    #     transforms.ToTensor(), # ToTensor : PIL image or numpy.ndarray를 tensor로 바꿈
    #     transforms.Normalize((fashion_mnist.mean()/255,), (fashion_mnist.std()/255,))])

    train_loader = DataLoader(torchvision.datasets.FashionMNIST(
        download=True, # 인터넷으로부터 데이터 다운
        root=".", # data가 저장될 경로(path)
        # transform=data_transform, # feature 및 label 변환(transformation) 지정
        train=True), # train set
        batch_size=train_batch_size, 
        shuffle=True)

    val_loader = DataLoader(torchvision.datasets.FashionMNIST(
        download=False, 
        root=".", 
        # transform=data_transform, 
        train=False),
        batch_size=val_batch_size, 
        shuffle=False)

    return train_loader, val_loader


class Net(nn.Module):
    def __init__(self):
      super(Net, self).__init__()
      self.conv1 = nn.Conv2d(1, 32, 3, 1)
      self.conv2 = nn.Conv2d(32, 64, 3, 1)
    #   self.dropout1 = nn.Dropout2d(0.25)
    #   self.dropout2 = nn.Dropout2d(0.5)
      self.fc1 = nn.Linear(576, 128)
      self.fc2 = nn.Linear(128, 10)

    # x는 데이터를 나타냅니다.
    def forward(self, x):
      # 데이터가 conv1을 지나갑니다.
      x = self.conv1(x)
      # x를 ReLU 활성함수(rectified-linear activation function)에 대입합니다.
      x = F.relu(x)

      x = self.conv2(x)
      x = F.relu(x)

      # x에 대해서 max pooling을 실행합니다.
      x = F.max_pool2d(x, 2)
      # 데이터가 dropout1을 지나갑니다.
      # x = self.dropout1(x)
      # start_dim=1으로 x를 압축합니다.
      x = torch.flatten(x, 1)
      # 데이터가 fc1을 지나갑니다.
      x = self.fc1(x)
      x = F.relu(x)
      # x = self.dropout2(x)
      x = self.fc2(x)

      # x에 softmax를 적용합니다.
      # output = F.log_softmax(x, dim=1)

      return x

# 임의의 28x28 이미지로 맞춰줍니다.
random_data = torch.rand((1, 1, 10, 10))
print(random_data)
my_nn = Net()
result = my_nn(random_data)
print (result)