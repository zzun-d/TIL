import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader 
import numpy as np

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

class CustomNet(nn.Module):
    def __init__(self, input, output):
        super().__init__()
        self.Layer1 = nn.Sequential(nn.Linear(input, 64), nn.Tanh())
        self.Layer2 = nn.Sequential(nn.Linear(64, 256), nn.Tanh())
        self.Layer3 = nn.Sequential(nn.Linear(256, 512), nn.Tanh())
        self.Layer3_1 = nn.Sequential(nn.Linear(512, 512), nn.Tanh())
        self.Layer4 = nn.Sequential(nn.Linear(512, 64), nn.Tanh())
        self.Layer5 = nn.Sequential(nn.Linear(64, output))
        self.flatten = nn.Flatten()

    def forward(self, x):
        x = self.flatten(x)
        x = self.Layer1(x)
        x = self.Layer2(x)
        x = self.Layer3(x)
        x = self.Layer3_1(x)
        x = self.Layer4(x)
        x = self.Layer5(x)
        return x
    


# 모델 생성
model = CustomNet(3**2, 3)
model.parameters()
model.train()


# 옵티마이저 정의
params = [param for param in model.parameters() if param.requires_grad]
optimizer = optim.SGD(params, lr = 0.001, momentum=0.9)

# 손실함수 정의
loss_fn = nn.MSELoss()

class CustomDataset(Dataset):

    def __init__(self):
        x_data = np.load('C:/Users/Junhyuk/ssafy08/TIL/밑바닥부터 시작하는 딥러닝/project/eigenvalue/input.npy')
        y_data = np.load('C:/Users/Junhyuk/ssafy08/TIL/밑바닥부터 시작하는 딥러닝/project/eigenvalue/output.npy')
        self.train_x = torch.tensor(x_data, dtype= torch.float32).to(device)
        self.train_y = torch.tensor(y_data, dtype= torch.float32).to(device)

    def __len__(self):
        return len(self.train_x)

    def __getitem__(self, idx):
        x = torch.FloatTensor(self.train_x[idx])
        y = torch.FloatTensor(self.train_y[idx])
        return x, y


dataset_custom = CustomDataset()

DataLoader(dataset_custom,            # Dataset 인스턴스가 들어감
           batch_size=8,       # 배치 사이즈를 설정
           shuffle=True,      # 데이터를 섞어서 사용하겠는지를 설정
           sampler=None,       # sampler는 index를 컨트롤
           batch_sampler=None, # 위와 비슷하므로 생략
           num_workers=2,      # 데이터를 불러올때 사용하는 서브 프로세스 개수
           collate_fn=None,    # map-style 데이터셋에서 sample list를 batch 단위로 바꾸기 위해 필요한 기능
           pin_memory=False,   # Tensor를 CUDA 고정 메모리에 할당
           drop_last=False,    # 마지막 batch를 사용 여부
           timeout=0,          # data를 불러오는데 제한시간
           worker_init_fn=None # 어떤 worker를 불러올 것인가를 리스트로 전달
          )

dataloader_custom = DataLoader(dataset_custom)



##########################################################
# 세번째 과제 Transfer Learning & Hyper Parameter Tuning # 
##########################################################

epochs = 10
for e in range(epochs):
    for i, Data in enumerate(dataloader_custom):
        output = model(Data[0])
        loss = loss_fn(output, Data[1])
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if i % 100 == 0:
            print('Epoch {}/{} Batch {}/{} Cost: {:.6f}'.format(
        e+1, 10, i+1, len(dataloader_custom),
        loss.item()
        ))
        