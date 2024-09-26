# 后端服务脚本
from fastapi import FastAPI
from pydantic import BaseModel

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
