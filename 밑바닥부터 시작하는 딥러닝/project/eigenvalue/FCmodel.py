import enum
from pickletools import optimize
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
import numpy as np

if torch.cuda.is_available():
    device = torch.device("cuda") 
else:
    device = torch.device("cpu")

x_data = np.load('C:/Users/Junhyuk/ssafy08/TIL/밑바닥부터 시작하는 딥러닝/project/eigenvalue/input.npy')
y_data = np.load('C:/Users/Junhyuk/ssafy08/TIL/밑바닥부터 시작하는 딥러닝/project/eigenvalue/output.npy')
train_x = torch.from_numpy(x_data) 
train_y = torch.from_numpy(y_data) 
train_x = torch.unsqueeze(train_x, 1)
# train_y = torch.unsqueeze(train_y, 1)


def get_data_loaders(train_batch_size):
    # fashion_mnist = torchvision.datasets.FashionMNIST(
    #     download=True, 
    #     train=True, 
    #     root=".").train_data.float()
    
    # data_transform = transforms.Compose([ # Compose : transforms 리스트 구성
    #     transforms.Resize((224, 224)), # Resize : 입력 이미지의 크기를 지정된 크기로 조정
    #     transforms.ToTensor(), # ToTensor : PIL image or numpy.ndarray를 tensor로 바꿈
    #     transforms.Normalize((fashion_mnist.mean()/255,), (fashion_mnist.std()/255,))])

    # train_loader = DataLoader(torchvision.datasets.FashionMNIST(
    #     download=True, # 인터넷으로부터 데이터 다운
    #     root=".", # data가 저장될 경로(path)
    #     # transform=data_transform, # feature 및 label 변환(transformation) 지정
    #     train=True), # train set
    #     batch_size=train_batch_size, 
    #     shuffle=True)

    train_loader = DataLoader(dataset, batch_size=train_batch_size)
    # val_loader = DataLoader(CustomDataset(test_x, test_y), batch_size=val_batch_size)

    return train_loader

class CustomDataset(Dataset):
    def __init__(self, train_x, train_y):
        self.x_data = [[73, 80, 75],
                       [93, 99, 93]]
        self.y_data = [[152], [185]]

    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):
        x = torch.FloatTensor(self.x_data[idx])
        y = torch.FloatTensor(self.y_data[idx])

        return x, y

dataset = CustomDataset(train_x, train_y,)



class Net(nn.Module):
    def __init__(self):
      super(Net, self).__init__()
      self.conv1 = nn.Conv2d(1, 32, 2, 1, 1)
      self.conv2 = nn.Conv2d(32, 64, 2, 1, 1)
      self.conv3 = nn.Conv2d(64, 128, 2, 1, 1)
      self.conv4 = nn.Conv2d(128, 64, 2, 1, 1)
      self.conv5 = nn.Conv2d(64, 32, 2, 1)
    #   self.conv3 = nn.Conv2d(64, 128, 2, 1)
    #   self.conv4 = nn.Conv2d(128, 128, 2, 1)
    #   self.conv5 = nn.Conv2d(128, 128, 2, 1)
    #   self.conv6 = nn.Conv2d(128, 128, 2, 1)
    #   self.conv7 = nn.Conv2d(128, 128, 2, 1)
    #   self.conv8 = nn.Conv2d(128, 64, 2, 1)
    #   self.conv9 = nn.Conv2d(64, 32, 2, 1)
    #   self.dropout1 = nn.Dropout2d(0.25)
    #   self.dropout2 = nn.Dropout2d(0.5)
      self.fc1 = nn.Linear(32, 64)
      self.fc2 = nn.Linear(64, 10)

    # x는 데이터를 나타냅니다.
    def forward(self, x):
        # 데이터가 conv1을 지나갑니다.
        print(f'ori: {x.size()}')
        x = self.conv1(x)
        # x를 ReLU 활성함수(rectified-linear activation function)에 대입합니다.
        x = F.relu(x)
        print(f'con1: {x.size()}')
        x = self.conv2(x)
        x = F.relu(x)
        print(f'con2: {x.size()}')
        x = self.conv3(x)
        x = F.relu(x)
        print(f'con3: {x.size()}')
        x = self.conv4(x)
        x = F.relu(x)
        print(f'con4: {x.size()}')
        x = self.conv5(x)
        x = F.relu(x)
        # x = self.conv6(x)
        # x = F.relu(x)
        # x = self.conv7(x)
        # x = F.relu(x)
        # x = self.conv8(x)
        # x = F.relu(x)
        # x = self.conv9(x)
        # x = F.relu(x)


        # x에 대해서 max pooling을 실행합니다.
        # x = F.max_pool2d(x, 2)
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

net = Net()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
epochs = 10
trainloader = get_data_loaders(1)
for epoch in range(10):
    running_loss = 0.0
    for i, data in enumerate(zip(train_x, train_y)):
        inputs, labels = data
        print(inputs, labels)
        print(type(inputs))
        print(inputs.size())
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print('Epoch {:4d}/{} Batch {}/{} Cost: {:.6f}'.format(
        epoch, 10, i+1, len(trainloader),
        loss.item()
        ))