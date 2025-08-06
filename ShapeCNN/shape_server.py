# FastAPI backend
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import torch
from torchvision import transforms
from PIL import Image
import io
import torch.nn as nn
import torch.nn.functional as F

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
    
model = ConvNeuralNetwork()
state_dict = torch.load('./model_weights.pth', map_location=torch.device('cpu')) # 가중치를 불러와서 model 에 적용 시키기 map_location cpu를 사용해서 cpu로 불러오기
model.load_state_dict(state_dict) # weight 불러온걸 적용
model.eval() # 테스트 검증 모드

CLASSES = ['cir', 'tri', 'x']

# 전처리 함수 파라미터에 프론트에서 사용자가 넣은 이미지를 넣음
def preprocess_image(image_bytes):
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.Grayscale(1),
        transforms.ToTensor(),
        transforms.RandomInvert(1),
        transforms.Normalize((0.5), (0.5))
    ])
    image = Image.open(io.BytesIO(image_bytes)).convert('L') # 이미지를 메모리에 올려 달라, 이미지를 byte 형식으로 , convert('L') = gray 스케일로?
    return transform(image).unsqueeze(0) # unsqueeze 차원을 하나 추가해서 return

app = FastAPI()

app.add_middleware( # CORS 포트 번호가 다를때
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        print(f"Received file: {file.filename}, size: {len(image_bytes)} bytes")
        
        input_tensor = preprocess_image(image_bytes)
        print(f"input tensor shape: {input_tensor.shape}")
        
        with torch.no_grad():
            outputs = model(input_tensor)
            print(f"Model outputs: {outputs}")
            
            _, predicted = torch.max(outputs, 1)
            label = CLASSES[predicted.item()]
            print(f"Predicted label: {label}")
        
        return JSONResponse(content={"label": label}) # 프론트쪽으로 JSON 형식으로 응답
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)