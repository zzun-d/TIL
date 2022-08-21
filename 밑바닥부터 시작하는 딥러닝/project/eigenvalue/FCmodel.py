from pickletools import optimize
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
import numpy as np

# 복소수 존재로 인하여 MSE 사용시 실수부, 복소수부 나눠서 MSE구하고 더하는 방식으로 진행해 보자.

if torch.cuda.is_available():
    device = torch.device("cuda") 
else:
    device = torch.device("cpu")

x_data = np.load('C:/Users/Junhyuk/ssafy08/TIL/밑바닥부터 시작하는 딥러닝/project/eigenvalue/input.npy')
y_data = np.load('C:/Users/Junhyuk/ssafy08/TIL/밑바닥부터 시작하는 딥러닝/project/eigenvalue/output.npy')
train_x = torch.from_numpy(x_data) 
train_y = torch.from_numpy(y_data)
train_x = torch.tensor(train_x, dtype= torch.float32)
train_y = torch.tensor(train_y, dtype= torch.float32).real
# train_x = torch.unsqueeze(train_x, 0)
# train_y = torch.unsqueeze(train_y, 0)
class CustomDataset(Dataset):
    def __init__(self, train_x, train_y):
        self.x_data = train_x
        self.y_data = train_y

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
        
        self.fc1 = nn.Linear(9, 64, bias=True)
        self.fc2 = nn.Linear(64, 128, bias=True)
        self.fc3 = nn.Linear(128, 256, bias=True)
        self.fc4 = nn.Linear(256, 256, bias=True)
        self.fc5 = nn.Linear(256, 64, bias=True)
        self.fc6 = nn.Linear(64, 1, bias=True)
        self.flatten = nn.Flatten(0, 1)
      
        torch.nn.init.kaiming_normal(self.fc1.weight.data)
        torch.nn.init.kaiming_normal(self.fc2.weight.data)
        torch.nn.init.kaiming_normal(self.fc3.weight.data)
        torch.nn.init.kaiming_normal(self.fc4.weight.data)
        torch.nn.init.kaiming_normal(self.fc5.weight.data)
        torch.nn.init.kaiming_normal(self.fc6.weight.data)
        

    # x는 데이터를 나타냅니다.
    def forward(self, x):
        # 데이터가 conv1을 지나갑니다.
        x = self.flatten(x)
        x = self.fc1(x)
        x = F.relu(x)
       
        x = self.fc2(x)
        x = F.relu(x)
       
        x = self.fc3(x)
        x = F.relu(x)
       
        x = self.fc4(x)
        x = F.relu(x)
       
        x = self.fc5(x)
        x = F.relu(x)
       
        x = self.fc6(x)
        x = F.relu(x)
       

        return x

net = Net()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)
epochs = 10
trainloader = DataLoader(dataset, 8, shuffle=False)

for epoch in range(10):
    running_loss = 0.0
    for i, data in enumerate(zip(train_x, train_y)):
        inputs, labels = data

        outputs = net(inputs)
        loss = criterion(outputs, labels)
        
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if i % 1000 == 0:
            print('Epoch {:4d}/{} Batch {}/{} Cost: {:.6f}'.format(
            epoch, 10, i+1, len(trainloader),
            loss.item()
            ))