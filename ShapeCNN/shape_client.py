# Gradio frontend
import gradio as gr
import requests
import io

def classify_with_backend(image):
    url = "http://127.0.0.1:8000/classify"
    image_bytes = io.BytesIO() # BytesIO 객체 생성 바이트형식으로 전달하기 위해
    image.save(image_bytes, format="PNG") # image_bytes 형식, PNG 형식으로
    image_bytes = image_bytes.getvalue() 
    response = requests.post(url, files={"file": ("image.png", image_bytes, "image/png")}) #  "image/png" 헤더부분, 보낸뒤 응답 받기
    if response.status_code == 200: # 응답이 정상이면 실행할 IF 문
        return response.json().get("label", "Error") # label 있으면 label, 없으면 error
    else:
        return "Error"

iface = gr.Interface( # 화면 그라디오 인터페이스
    fn=classify_with_backend, # 위에서 정의한 함수
    inputs=gr.Image(type="pil"), # 이미지 입력 박스
    outputs="text", # 응답받은 response 를 text 로
    title="손글씨 도형 분류하기",
    description="○, X, △ 이미지를 넣어주세요 !!"
)

if __name__ == "__main__":
    iface.launch()