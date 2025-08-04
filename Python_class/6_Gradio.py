import gradio as gr

def add(num1,num2):
    return num1 + num2

# interface 모드를 하면 flag가 생김 flag를 클릭하면 csv파일에 데이터가 저장된다.
interface = gr.Interface(
    # submit 을 클릭하면 등록한 add 함수가 출력
    fn=add,
    inputs=['number', 'number'],
    outputs='number',
    title='Cal',
    description='숫자 두 개를 입력하세요',
    flagging_mode="never" # flag를 하지않음
)

interface.launch()