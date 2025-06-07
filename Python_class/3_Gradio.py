import gradio as gr

def handle_input(text):
    return text

with gr.Blocks() as demo:
    # text_input 에 적은 데이터가 저장
    text_input = gr.Textbox(label='문자입력', lines=1)
    output_text = gr.Textbox(label='출력')
    text_input.submit(handle_input, inputs=text_input, outputs=output_text)



demo.launch()