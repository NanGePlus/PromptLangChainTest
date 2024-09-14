import requests
import json
import logging


# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


url = "http://localhost:8012/v1/chat/completions"
headers = {"Content-Type": "application/json"}

# 默认非流式输出 True or False
stream_flag = False

# input_text = """
# 用户：你们有什么流量大的套餐
# 客服：您好，我们现在正在推广无限套餐，每月300元就可以享受1000G流量，您感兴趣吗
# """

input_text = """
用户：你们有什么流量大的套餐
客服：您好，我们现在正在推广无限套餐，每月300元,您感兴趣吗
"""

# 第一次请求
data = {
    "messages": [{"role": "user", "content": input_text}],
    "stream": stream_flag
}


# 接收流式输出
if stream_flag:
    try:
        with requests.post(url, stream=True, headers=headers, data=json.dumps(data)) as response:
            for line in response.iter_lines():
                if line:
                    json_str = line.decode('utf-8').strip("data: ")
                    # 检查是否为空或不合法的字符串
                    if not json_str:
                        logger.info(f"收到空字符串，跳过...")
                        continue
                    # 确保字符串是有效的JSON格式
                    if json_str.startswith('{') and json_str.endswith('}'):
                        try:
                            data = json.loads(json_str)
                            if data['choices'][0]['finish_reason'] == "stop":
                                logger.info(f"接收JSON数据结束")
                            else:
                                logger.info(f"流式输出，响应内容是: {data['choices'][0]['delta']['content']}")
                        except json.JSONDecodeError as e:
                            logger.info(f"JSON解析错误: {e}")
                    else:
                        print(f"无效JSON格式: {json_str}")
    except Exception as e:
        print(f"Error occurred: {e}")

# 接收非流式输出处理
else:
    # 发送post请求
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # logger.info(f"接收到返回的响应原始内容: {response.json()}\n")
    content = response.json()['choices'][0]['message']['content']
    logger.info(f"非流式输出，响应内容是: {content}\n")