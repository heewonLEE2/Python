import gradio as gr
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY")
)

# 이런 형식으로 번역 해달라고 예제를 적음
example = {
    "한국어" : ["오늘 날씨어때?", "최근 멀티모달 AI 기술이 인기를 끌고 있다."],
    "영어" : ["How is the weather today?","Recently, multimodal AI technology has become popular."],
    "일본어" : ["今日の天気はどう？","最近、マルチモーダルAI技術が人気を集めている。"]
}

def translate_text_chatgpt(text, src_lang, trg_lang):
    def build_fewshot(src_lang, trg_lang):
        src_examples = example[src_lang]
        trg_examples = example[trg_lang]
        fewshot_messages = []
        for src_text, trg_text in zip(src_examples, trg_examples):
            # 유저가 말하는 부분에대해 assistant 으로 대답
            fewshot_messages.append({"role":"user", "content":src_text})
            fewshot_messages.append({"role":"assistant","content":trg_text})
        return fewshot_messages
    
    system_instruction = f'assistant는 번역앱으로 동작한다. {src_lang}를 {trg_lang}로 적절하게 번역된 텍스트만 출력한다.'
    fewshot_messages = build_fewshot(src_lang=src_lang, trg_lang=trg_lang)
    messages = [{"role":"system", "content":system_instruction}, *fewshot_messages, {"role":"user", "content":text}]
    # print(messages)
    # GPT 모델에서 받은 response
    response = client.chat.completions.create(
        model="gpt-4.1-2025-04-14",
        messages= messages
    )
    return response.choices[0].message.content

def gradio_translate(text, src_lang, trg_lang):
    if not text.strip():
        return '번역할 내용을 입력하세요'
    if src_lang ==  trg_lang:
        return '원본 언어와 번역 언어가 같습니다. 다른 언어를 선택하세요'
    return translate_text_chatgpt(text, src_lang, trg_lang)

with gr.Blocks() as demo:
    gr.Markdown('# 초간단 번역 앱')
    text_input = gr.Textbox(label="번역할 내용을 입력하세요", placeholder="여기에 내용을 입력하세요")
    # 번역 하고 싶은 문장
    src_lang_dropdown = gr.Dropdown(choices=['한국어', '영어', '일본어'], value="영어", label="번역할 언어를 선택하세요")
    trg_lang_dropdown = gr.Dropdown(choices=['영어', '한국어', '일본어'], value='한국어', label='번역된 언어를 선택하세요')
    translate_button = gr.Button('번역하기')
    output_text = gr.Textbox(label="번역된 결과", placeholder="번역된 결과가 여기에 표시됩니다.", interactive=False)

    translate_button.click(
        gradio_translate, inputs = [text_input, src_lang_dropdown, trg_lang_dropdown],
        outputs = output_text
    )

demo.launch()