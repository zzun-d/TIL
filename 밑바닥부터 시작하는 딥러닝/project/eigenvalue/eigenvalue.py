import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
import torch.nn as nn

x_data = np.load('C:/Users/Junhyuk/ssafy08/TIL/밑바닥부터 시작하는 딥러닝/project/eigenvalue/input.npy')
y_data = np.load('C:/Users/Junhyuk/ssafy08/TIL/밑바닥부터 시작하는 딥러닝/project/eigenvalue/output.npy')

train_x = x_data[:8000]
train_y = y_data[:8000]

test_x = x_data[8000:]
test_y = y_data[8000:]

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = nn.Linear()
    def forward():
        1
    

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.x_data = train_x
        self.y_data = train_y

    
    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):
        x = torch.FloatTensor(self.x_data[idx])
        y = torch.FloatTensor(self.y_data[idx])
        return x, y

dataset = CustomDataset()
dataloader = DataLoader(dataset, batch_size=1)

model = MyModel()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)

epochs = 20

for epoch in range(epochs):
    for batch_idx, samples in enumerate(dataloader):
        x_train, y_train = samples
        prediction = model(torch.flatten(x_train))

        cost = F.mse_loss(prediction, y_train)

        optimizer.zero_grad()
        cost.backward()
        optimizer.step()

        print('Epoch {:4d}/{} Batch {}/{} Cost: {:.6f}'.format(
            epoch, epochs, batch_idx, len(dataloader), cost.item()
        ))