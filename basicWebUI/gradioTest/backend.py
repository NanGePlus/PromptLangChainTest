# 后端服务脚本
from fastapi import FastAPI
from pydantic import BaseModel
import logging
import uvicorn


# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PORT = 8012  # 服务访问的端口

# 创建 FastAPI 实例
app = FastAPI()

# 定义请求体模型
class TextInput(BaseModel):
    text: str

# 定义一个处理文本的接口
@app.post("/process_text")
def process_text(input: TextInput):
    # 模拟文本处理逻辑，比如将输入文本转为大写
    processed_text = input.text.upper()
    return {"processed_text": processed_text}

if __name__ == "__main__":
    logger.info(f"在端口 {PORT} 上启动服务器")
    # uvicorn是一个用于运行ASGI应用的轻量级、超快速的ASGI服务器实现
    # 用于部署基于FastAPI框架的异步PythonWeb应用程序
    uvicorn.run(app, host="0.0.0.0", port=PORT)

