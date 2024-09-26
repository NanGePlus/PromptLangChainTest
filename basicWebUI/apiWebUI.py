import gradio as gr
import requests
import json
import logging

# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 后端服务接口地址
url = "http://localhost:8012/v1/chat/completions"
headers = {"Content-Type": "application/json"}

# 默认非流式输出 True or False
stream_flag = False


# 定义发送消息到后端的方法，并更新聊天记录
def send_message(user_message, chat_history):
    # 请求数据
    data = {
        "messages": [{"role": "user", "content": user_message}],
        "stream": stream_flag,
        "userId": "123",
        "conversationId": "123"
    }

    # 更新聊天记录，添加用户消息
    chat_history.append(["user", user_message])

    # 接收非流式输出处理
    try:
        # 发送 POST 请求到后端
        response = requests.post(url, headers=headers, data=json.dumps(data))
        # 解析响应数据
        response_text = response.json()['choices'][0]['message']['content']
        logger.info(f"非流式输出，响应内容是: {response_text}\n")

        # 更新聊天记录，添加助手回复
        chat_history.append(["assistant", response_text])
        return chat_history
    except Exception as e:
        error_message = f"请求失败: {e}"
        logger.error(error_message)
        chat_history.append(["assistant", error_message])
        return chat_history


# Gradio 前端界面
with gr.Blocks() as demo:
    # 聊天框，初始为空
    chatbox = gr.Chatbot(label="聊天对话")

    # 用户输入框
    with gr.Row():
        with gr.Column(scale=8):
            user_input = gr.Textbox(label="请输入消息", placeholder="在此输入您的消息")
        with gr.Column(scale=2):
            send_button = gr.Button("发送")

    # 绑定按钮点击事件到 send_message 函数，并清空输入框
    send_button.click(send_message, inputs=[user_input, chatbox], outputs=chatbox)
    send_button.click(lambda: "", None, user_input)  # 清空输入框

    # 提交消息时更新聊天记录并清空输入框
    user_input.submit(send_message, inputs=[user_input, chatbox], outputs=chatbox)
    user_input.submit(lambda: "", None, user_input)

# 启动 Gradio 前端
if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
