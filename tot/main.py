# 功能说明：实现使用langchain框架，模拟实现客服质量检查(进阶技巧-思维链 Chain of Thoughts)
# 用于分析候选人在速度、耐力、力量等方面的素质，并通过调用一系列链（chain）来确定适合候选人的运动项目

import os
import re
import json
import asyncio
import uuid
import time
import logging
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from langchain_openai import ChatOpenAI
# prompt模版
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
# 部署REST API相关
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
import uvicorn

from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser



# 设置langsmith环境变量
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = "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"

# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# prompt模版设置相关 根据自己的实际情况进行调整
PROMPT_TEMPLATE_TXT_ANALYSER = "prompt_template_performanceAnalyser.txt"
PROMPT_TEMPLATE_TXT_SPORTS = "prompt_template_possibleSports.txt"
PROMPT_TEMPLATE_TXT_EVALUATE = "prompt_template_evaluate.txt"
PROMPT_TEMPLATE_TXT_REPORT = "prompt_template_reportGenerator.txt"

# 模型设置相关  根据自己的实际情况进行调整
API_TYPE = "oneapi"  # openai:调用gpt模型；oneapi:调用oneapi方案支持的模型(这里调用通义千问)
# openai模型相关配置 根据自己的实际情况进行调整
OPENAI_API_BASE = "https://api.wlai.vip/v1"
OPENAI_CHAT_API_KEY = "sk-EhxvNWXkjzZJADfHA1Ac24Dd0f0b42B2B97f3725D3BcA378"
OPENAI_CHAT_MODEL = "gpt-4o-mini"
# oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整
ONEAPI_API_BASE = "http://139.224.72.218:3000/v1"
ONEAPI_CHAT_API_KEY = "sk-kejMo1NVoYEYFt5rD4E9Ff9c887e413994Be087cAbAdEd6b"
ONEAPI_CHAT_MODEL = "qwen-max"

# API服务设置相关  根据自己的实际情况进行调整
PORT = 8012  # 服务访问的端口

# 申明全局变量 全局调用
model = None  # 使用的LLM模型

prompt_performanceAnalyser = None  # prompt内容
performanceAnalyser_chain = None  # 定义的chain
prompt_possibleSports = None  # prompt内容
possibleSports_chain = None  # 定义的chain
prompt_evaluate = None  # prompt内容
evaluate_chain = None  # 定义的chain
prompt_report = None  # prompt内容
report_chain = None  # 定义的chain



# 定义Message类
class Message(BaseModel):
    role: str
    name: str
    performance: str
    category: str

class ResponseChoiceMessage(BaseModel):
    role: str
    content: str

# 定义ChatCompletionRequest类
class ChatCompletionRequest(BaseModel):
    messages: List[Message]
    stream: Optional[bool] = False

# 定义ChatCompletionResponseChoice类
class ChatCompletionResponseChoice(BaseModel):
    index: int
    message: ResponseChoiceMessage
    finish_reason: Optional[str] = None

# 定义ChatCompletionResponse类
class ChatCompletionResponse(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{uuid.uuid4().hex}")
    object: str = "chat.completion"
    created: int = Field(default_factory=lambda: int(time.time()))
    choices: List[ChatCompletionResponseChoice]
    system_fingerprint: Optional[str] = None


# 获取prompt在chain中传递的prompt最终的内容
def getPrompt(prompt):
    logger.info(f"最后给到LLM的prompt的内容: {prompt}")
    return prompt


# 格式化响应，对输入的文本进行段落分隔、添加适当的换行符，以及在代码块中增加标记，以便生成更具可读性的输出
def format_response(response):
    # 使用正则表达式 \n{2, }将输入的response按照两个或更多的连续换行符进行分割。这样可以将文本分割成多个段落，每个段落由连续的非空行组成
    paragraphs = re.split(r'\n{2,}', response)
    # 空列表，用于存储格式化后的段落
    formatted_paragraphs = []
    # 遍历每个段落进行处理
    for para in paragraphs:
        # 检查段落中是否包含代码块标记
        if '```' in para:
            # 将段落按照```分割成多个部分，代码块和普通文本交替出现
            parts = para.split('```')
            for i, part in enumerate(parts):
                # 检查当前部分的索引是否为奇数，奇数部分代表代码块
                if i % 2 == 1:  # 这是代码块
                    # 将代码块部分用换行符和```包围，并去除多余的空白字符
                    parts[i] = f"\n```\n{part.strip()}\n```\n"
            # 将分割后的部分重新组合成一个字符串
            para = ''.join(parts)
        else:
            # 否则，将句子中的句点后面的空格替换为换行符，以便句子之间有明确的分隔
            para = para.replace('. ', '.\n')
        # 将格式化后的段落添加到formatted_paragraphs列表
        # strip()方法用于移除字符串开头和结尾的空白字符（包括空格、制表符 \t、换行符 \n等）
        formatted_paragraphs.append(para.strip())
    # 将所有格式化后的段落用两个换行符连接起来，以形成一个具有清晰段落分隔的文本
    return '\n\n'.join(formatted_paragraphs)


# 定义了一个异步函数lifespan，它接收一个FastAPI应用实例app作为参数。这个函数将管理应用的生命周期，包括启动和关闭时的操作
# 函数在应用启动时执行一些初始化操作，如设置搜索引擎、加载上下文数据、以及初始化问题生成器
# 函数在应用关闭时执行一些清理操作
# @asynccontextmanager 装饰器用于创建一个异步上下文管理器，它允许你在 yield 之前和之后执行特定的代码块，分别表示启动和关闭时的操作
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    # 申明引用全局变量，在函数中被初始化，并在整个应用中使用
    global model, API_TYPE
    global prompt_performanceAnalyser, performanceAnalyser_chain
    global prompt_possibleSports, possibleSports_chain
    global prompt_evaluate, evaluate_chain
    global prompt_report, report_chain

    global PROMPT_TEMPLATE_TXT_ANALYSER,PROMPT_TEMPLATE_TXT_SPORTS,PROMPT_TEMPLATE_TXT_EVALUATE,PROMPT_TEMPLATE_TXT_REPORT
    global ONEAPI_API_BASE, ONEAPI_CHAT_API_KEY, ONEAPI_CHAT_MODEL
    global OPENAI_API_BASE, OPENAI_CHAT_API_KEY, OPENAI_CHAT_MODEL
    # 根据自己实际情况选择调用model和embedding模型类型
    try:
        logger.info("正在初始化模型、提取prompt模版、定义chain...")
        # （1）根据API_TYPE选择初始化对应的模型
        if API_TYPE == "oneapi":
            # 实例化一个oneapi客户端对象
            model = ChatOpenAI(
                base_url=ONEAPI_API_BASE,
                api_key=ONEAPI_CHAT_API_KEY,
                model=ONEAPI_CHAT_MODEL,  # 本次使用的模型
                temperature=0.8,# 发散的程度，一般为0
                # response_format={"type": response_format},
            )
        elif API_TYPE == "openai":
            # 实例化一个ChatOpenAI客户端对象
            model = ChatOpenAI(
                base_url=OPENAI_API_BASE,# 请求的API服务地址
                api_key=OPENAI_CHAT_API_KEY,# API Key
                model=OPENAI_CHAT_MODEL,# 本次使用的模型
                temperature=0.8,# 发散的程度，一般为0
                # response_format={"type": response_format},
            )

        # （2）提取prompt模版
        prompt_template_performanceAnalyser = PromptTemplate.from_file(PROMPT_TEMPLATE_TXT_ANALYSER)
        prompt_template_possibleSports = PromptTemplate.from_file(PROMPT_TEMPLATE_TXT_SPORTS)
        prompt_template_evaluate = PromptTemplate.from_file(PROMPT_TEMPLATE_TXT_EVALUATE)
        prompt_template_report = PromptTemplate.from_file(PROMPT_TEMPLATE_TXT_REPORT)

        # 模版1
        prompt_performanceAnalyser = ChatPromptTemplate.from_messages(
            [
                ("human", prompt_template_performanceAnalyser.template)
            ]
        )
        # 模版2
        prompt_possibleSports = ChatPromptTemplate.from_messages(
            [
                ("human", prompt_template_possibleSports.template)
            ]
        )
        # 模版3
        prompt_evaluate = ChatPromptTemplate.from_messages(
            [
                ("human", prompt_template_evaluate.template)
            ]
        )
        # 模版4
        prompt_report = ChatPromptTemplate.from_messages(
            [
                ("human", prompt_template_report.template)
            ]
        )

        # （3）定义chain
        performanceAnalyser_chain = prompt_performanceAnalyser | model
        possibleSports_chain = prompt_possibleSports | model
        evaluate_chain = prompt_evaluate | model
        report_chain = prompt_report | model

        logger.info("初始化完成")
    except Exception as e:
        logger.error(f"初始化过程中出错: {str(e)}")
        # raise 关键字重新抛出异常，以确保程序不会在错误状态下继续运行
        raise

    # yield 关键字将控制权交还给FastAPI框架，使应用开始运行
    # 分隔了启动和关闭的逻辑。在yield 之前的代码在应用启动时运行，yield 之后的代码在应用关闭时运行
    yield
    # 关闭时执行
    logger.info("正在关闭...")


# lifespan参数用于在应用程序生命周期的开始和结束时执行一些初始化或清理工作
app = FastAPI(lifespan=lifespan)


# POST请求接口，与大模型进行知识问答
@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    # 申明引用全局变量，在函数中被初始化，并在整个应用中使用
    if not model or not prompt_performanceAnalyser or not performanceAnalyser_chain:
        logger.error("服务未初始化")
        raise HTTPException(status_code=500, detail="服务未初始化")

    try:
        logger.info(f"收到聊天完成请求: {request}")

        # 解析出发送请求体中的参数
        name = request.messages[-1].name
        performance = request.messages[-1].performance
        category = request.messages[-1].category

        # 第一步:调用chain分析候选人在速度、耐力、力量三方面素质的分档分数
        result = performanceAnalyser_chain.invoke(
            {"text": name+performance}
        )
        # logger.info(f"result: {result.content}")
        # 使用正则表达式提取完整的JSON内容,并进行json格式化处理
        json_content = re.search(r'\{[^}]+\}', result.content, re.DOTALL).group()
        talents = json.loads(json_content)
        logger.info(f"talents: {talents}")

        # 第二步:第一层节点遍历,对每个符合要求的素质获取可能适合的运动项目
        # 创建一个集合cache来存储已经处理过的运动项目，以避免重复处理
        cache = set()
        finalContent  =  ''

        for k, v in talents.items():
            if v < 3:  # 如果分数小于3，则跳过（剪枝），避免处理不合格的素质
                continue
            # 获取指定能力素质和指定的运动类别(拳击)适合的运动项目
            result = possibleSports_chain.invoke(
                {"talent": k,"category": category}
            )
            # logger.info(f"result: {result.content}")
            # 使用正则表达式提取完整的JSON内容,并进行json格式化处理
            json_content = re.search(r'\{[^}]+\}', result.content, re.DOTALL).group()
            leafs = json.loads(json_content)
            logger.info(f"leafs: {leafs}")
            # 将获取到的运动名称添加到sports_list中
            sports_list = []
            for key, values in leafs.items():
                sports_list.extend(values)
            logger.info(f"sports_list: {sports_list}")

            # 第三步 第二层节点遍历
            # 对于每个运动项目，检查其他素质是否适合这个运动项目
            # 如果 p（当前素质的分数）不大于 val（评估链返回的分数），则将 suitable 设为 False 并跳出循环（剪枝）
            for sports in sports_list:
                if sports in cache:
                    continue
                cache.add(sports)
                suitable = True
                for t, p in talents.items():
                    if t == k:
                        continue
                    result = evaluate_chain.invoke(
                        {"sports": sports, "talent": t}
                    )
                    # logger.info(f"evaluate_result: {result.content}")
                    val = int(result.content)
                    logger.info(f"evaluate_result:{sports}: {t} {val} {p >= val}")
                    if not p>=val:  # 剪枝
                        suitable = False
                        break
                logger.info(f"suitable: {suitable}")

                # 第四步:如果当前运动项目适合候选人，则调用生成报告，并记录生成的报告内容
                if suitable:
                    result = report_chain.invoke(
                        {"name": name, "performance": performance, "talents": talents, "sports": sports }
                    )
                    logger.info(f"report_result: {result.content}")

                    finalContent = finalContent + str(format_response(result.content))

        # formatted_response = str(format_response(result.content))
        formatted_response = finalContent
        logger.info(f"格式化的搜索结果: {formatted_response}")

        # 处理流式响应
        if request.stream:
            # 定义一个异步生成器函数，用于生成流式数据
            async def generate_stream():
                # 为每个流式数据片段生成一个唯一的chunk_id
                chunk_id = f"chatcmpl-{uuid.uuid4().hex}"
                # 将格式化后的响应按行分割
                lines = formatted_response.split('\n')
                # 历每一行，并构建响应片段
                for i, line in enumerate(lines):
                    # 创建一个字典，表示流式数据的一个片段
                    chunk = {
                        "id": chunk_id,
                        "object": "chat.completion.chunk",
                        "created": int(time.time()),
                        # "model": request.model,
                        "choices": [
                            {
                                "index": 0,
                                "delta": {"content": line + '\n'}, # if i > 0 else {"role": "assistant", "content": ""},
                                "finish_reason": None
                            }
                        ]
                    }
                    # 将片段转换为JSON格式并生成
                    yield f"{json.dumps(chunk)}\n"
                    # 每次生成数据后，异步等待0.5秒
                    await asyncio.sleep(0.5)
                # 生成最后一个片段，表示流式响应的结束
                final_chunk = {
                    "id": chunk_id,
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "choices": [
                        {
                            "index": 0,
                            "delta": {},
                            "finish_reason": "stop"
                        }
                    ]
                }
                yield f"{json.dumps(final_chunk)}\n"

            # 返回fastapi.responses中StreamingResponse对象，流式传输数据
            # media_type设置为text/event-stream以符合SSE(Server-SentEvents) 格式
            return StreamingResponse(generate_stream(), media_type="text/event-stream")
        # 处理非流式响应处理
        else:
            response = ChatCompletionResponse(
                choices=[
                    ChatCompletionResponseChoice(
                        index=0,
                        # message=Message(role="assistant", content=formatted_response),
                        message=ResponseChoiceMessage(role="assistant", content=formatted_response),
                        finish_reason="stop"
                    )
                ]
            )
            logger.info(f"发送响应内容: \n{response}")
            # 返回fastapi.responses中JSONResponse对象
            # model_dump()方法通常用于将Pydantic模型实例的内容转换为一个标准的Python字典，以便进行序列化
            return JSONResponse(content=response.model_dump())
    except Exception as e:
        logger.error(f"处理聊天完成时出错:\n\n {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    logger.info(f"在端口 {PORT} 上启动服务器")
    # uvicorn是一个用于运行ASGI应用的轻量级、超快速的ASGI服务器实现
    # 用于部署基于FastAPI框架的异步PythonWeb应用程序
    uvicorn.run(app, host="0.0.0.0", port=PORT)


