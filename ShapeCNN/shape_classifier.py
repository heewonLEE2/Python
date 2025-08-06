# 1. 딥러닝 모델 서빙
'''
딥러닝 모델 서빙(DL Model Serving)은 학습된 머신러닝 모델을 실시간 또는 비실시간으로 애플리케이션에서 사용할 수 있도록 배포하고, 입력 데이터에 대한 예측을 제공하는 프로세스를 말합니다. 이를 위해 모델은 주로 REST API, gRPC, 혹은 WebSocket 같은 네트워크 인터페이스를 통해 호출될 수 있는 상태로 배포됩니다. 모델 서빙 시스템은 입력 데이터를 전처리하고 모델에 전달한 후, 출력 결과를 후처리하여 클라이언트에 반환하는 과정을 자동화하며, 일반적으로 안정성, 확장성, 낮은 지연 시간을 보장하도록 설계됩니다.
'''

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader

transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.Grayscale(1),
    transforms.ToTensor(),
    transforms.RandomInvert(1),
    transforms.Normalize((0.5), (0.5))
])

train_path = 'C:\\heewon\\FastAPI\\shape\\train'
test_path = 'C:\\heewon\\FastAPI\\shape\\test'

trainset = torchvision.datasets.ImageFolder(root=train_path, transform=transform)
testset = torchvision.datasets.ImageFolder(root=test_path, transform=transform)

class_map = {0: 'cir', 1:'tri', 2:'x'}

loader = DataLoader(
    dataset = trainset,
    batch_size = 64,
    shuffle=True
)

class ConvNeuralNetwork(nn.Module):
    def __init__(self):
        super(ConvNeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.classifier = nn.Sequential(
            nn.Conv2d(1, 28, kernel_size=3, padding='same'),
            nn.ReLU(),

            nn.Conv2d(28, 28, kernel_size=3, padding='same'),
            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2),
            nn.Dropout(0.25),

            nn.Conv2d(28, 56, kernel_size=3, padding='same'),
            nn.ReLU(),

            nn.Conv2d(56, 56, kernel_size=3, padding='same'), # (56, 14, 14)
            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2), # (56, 7, 7)
            nn.Dropout(0.25),
        )
        self.Linear = nn.Linear(56 * 7 * 7, 3)
    
    def forward(self, x):
        x = self.classifier(x)
        x = self.flatten(x)
        output = self.Linear(x)
        return output
    
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = ConvNeuralNetwork().to(device)

loss = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

def train_loop(train_loader, model, loss_fn, optimizer):
    sum_losses = 0
    sum_accs = 0
    for x_batch, y_batch in train_loader:
        x_batch = x_batch.to(device)
        y_batch = y_batch.to(device)
        y_pred = model(x_batch)
        loss = loss_fn(y_pred, y_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        sum_losses = sum_losses + loss

        y_prob = nn.Softmax(1)(y_pred)
        y_pred_index = torch.argmax(y_prob, axis=1)
        acc = (y_batch == y_pred_index).float().sum() / len(y_batch) * 100
        sum_accs = sum_accs + acc
    
    avg_loss = sum_losses / len(train_loader)
    avg_acc = sum_accs / len(train_loader)
    return avg_loss, avg_acc


epochs = 50

for i in range(epochs):
    print(f"------------------------------------------------")
    avg_loss, avg_acc = train_loop(loader, model, loss, optimizer)
    print(f'Epoch {i:4d}/{epochs} Loss: {avg_loss:.6f} Accuracy: {avg_acc:.2f}%')
print("Done!")

test_loader = DataLoader(
    dataset=testset,
    batch_size=32,
    shuffle=False
)

torch.save(model.state_dict(), 'model_weights.pth')
torch.save(model, 'model.pt')