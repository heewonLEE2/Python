import gradio as gr

def handel_checkbox(selected):
    if selected:
        return "동의했습니다.!"
    return "동의하지 않았습니다."

with gr.Blocks() as demo:
    checkbox = gr.Checkbox(label="개인정보 사용에 동의하겠습니까")
    output_checkbox = gr.Textbox(label="출력")
    # 체크 박스가 change하는지에 따라서
    checkbox.change(handel_checkbox, inputs=checkbox, outputs=output_checkbox)

demo.launch()