import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# 안녕하세요")
    gr.Markdown("## 여기는 제목을 입력합니다.")
    gr.Markdown("- 첫번째 아이템\n- 두번째 아이템\n- 세번째 아이템")



demo.launch()