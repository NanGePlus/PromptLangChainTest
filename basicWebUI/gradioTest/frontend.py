# 前端页面脚本
import gradio as gr
import requests


# 定义一个调用 FastAPI 接口的函数
def process_text_gradio(input_text):
    # FastAPI 接口的 URL
    url = "http://127.0.0.1:8000/process_text"

    # 将输入文本传递给 FastAPI 接口
    response = requests.post(url, json={"text": input_text})

    # 提取返回的处理后的文本
    processed_text = response.json()["processed_text"]

    return processed_text


# 使用 Gradio 创建一个简单的前端页面
with gr.Blocks() as demo:
    # 文本输入框
    input_text = gr.Textbox(label="输入文本")

    # 输出文本框
    output_text = gr.Textbox(label="处理后的文本")

    # 按钮点击事件，调用 process_text_gradio 函数
    submit_button = gr.Button("提交")
    submit_button.click(process_text_gradio, inputs=input_text, outputs=output_text)

# 启动 Gradio 前端
if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
