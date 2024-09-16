# 0、相关视频链接        
(1)【大模型应用开发基础】集成开发环境搭建Anaconda+PyCharm                   
https://www.bilibili.com/video/BV1q9HxeEEtT/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                  
https://youtu.be/myVgyitFzrA                
(2)【基础-模拟智能推荐客服】本系列视频主要介绍prompt工程相关基础及进阶用例，旨在帮助大家更好地了解和使用prompt。一份代码同时支持GPT和各国产大模型                                        
https://www.bilibili.com/video/BV1zWH1e6ETp/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                              
https://youtu.be/mSG7X32CeGA                  
(3)【进阶-短期、长期记忆】本系列视频主要介绍prompt工程相关基础及进阶用例，旨在帮助大家更好地了解和使用prompt。一份代码同时支持GPT和各国产大模型             
https://www.bilibili.com/video/BV1pWH4eZEN6/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                 
https://youtu.be/C2r1bIVJzr0                
(4)【进阶-思维链(Chain of Thoughts CoT) 】本系列视频主要介绍prompt工程相关基础及进阶用例，旨在帮助大家更好地了解和使用prompt                 
https://www.bilibili.com/video/BV1akpgeeEpG/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                                                 
https://youtu.be/YrOL2eIWw7c                  
(5)【进阶-自洽性(Self-Consistency) 】本系列视频主要介绍prompt工程相关基础及进阶用例，旨在帮助大家更好地了解和使用prompt                                            
https://www.bilibili.com/video/BV1d9tKeuEBf/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                                                   
https://youtu.be/Ev-S8AMo_ts                                                        

# 1、基础概念
## 1.1 prompt基础
### (1) prompt定义
prompt就是你发给大模型的指令，比如编写个故事、讲个笑话、写份报告等                                                
**貌似简单，但意义非凡**                            
(1)prompt是AGI时代的编程语言                                                               
(2)prompt工程是AGI时代的软件工程                        
(3)prompt工程师是AGI时代的程序员                           
学会prompt工程，就像学用鼠标、键盘一样，是AGI时代的基本技能                               
prompt工程门槛低，天花板高，所以有人戏称prompt为咒语                                 

### (2) 我们的优势
我们把AI当人看,所以知道:                     
(1)为什么有的指令有效，有的指令无效(你去做那个吧?  你去帮我介绍下prompt概念?)                                 
(2)为什么同样的指令有时有效，有时无效(请告诉我Java的特点)                
可能的回答1：Java是一种广泛使用的编程语言，具有跨平台性、面向对象等特点                           
可能的回答2：爪哇（Java）是印度尼西亚的一个岛屿，以其丰富的文化和历史而闻名                           
(3)怎么提升指令有效的概率               
我们懂编程,所以知道:                                
(1)知道哪些问题用prompt工程解决更高效，哪些用传统编程更高效                   
(2)能完成和业务系统的对接，把效能发挥到极致                          

### (3) prompt调优
找到好的prompt是个持续迭代的过程，需要不断调优         
如果知道训练数据是怎样的，参考训练数据来构造prompt是最好的                              
(1)把AI当人来看:你知道ta爱读西游记，就和ta聊西游记                                
(2)不知道训练数据怎么办？看Ta是否主动告诉你。例如OpenAI的GPT对Markdown格式友好                      
(3)还有一种方式就是不断试。有时一字之差，对生成概率的影响都可能是很大的，也可能毫无影响          
**试是常用方法，确实有运气因素，所以门槛低、天花板高**         
**高质量prompt核心要点：指令具体、信息丰富、尽量少歧义**         

### (4) prompt的典型构成
不要固守模版。模版的价值是提醒我们别漏掉什么，而不是必须遵守模版才行             
**角色:** 给AI定义一个最匹配任务的角色，比如:你是一位相声大师                           
**指示:** 对任务进行描述               
**上下文:** 给出与任务相关的其它背景信息（尤其在多轮交互中）             
**例子:** 必要时给出举例，学术中称为one-shot learning, few-shot learning或in-context learning；实践证明其对输出正确性有很大帮助           
**输入:** 任务的输入信息；在提示词中明确的标识出输入                  
**输出:** 输出的格式描述，以便后继模块自动解析模型的输出结果，比如（JSON、XML）        
大模型对prompt开头和结尾的内容更敏感，先定义角色，其实就是在开头把问题域收窄，减少二义性                                                    


## 1.2 LangChain
### （1）LangChain定义
LangChain是一个用于开发由大型语言模型(LLM)驱动的应用程序的框架，官方网址：https://python.langchain.com/v0.2/docs/introduction/          
### （2）LCEL定义
LCEL(LangChain Expression Language),原来叫chain，是一种申明式语言，可轻松组合不同的调用顺序构成chain            
其特点包括流支持、异步支持、优化的并行执行、重试和回退、访问中间结果、输入和输出模式、无缝LangSmith跟踪集成、无缝LangServe部署集成            
### （3）LangSmith
LangSmith是一个用于构建生产级LLM应用程序的平台。通过它，您可以密切监控和评估您的应用程序，官方网址：https://docs.smith.langchain.com/         



# 2、前期准备工作
## 2.1 anaconda、pycharm 安装   
anaconda:提供python虚拟环境，官网下载对应系统版本的安装包安装即可           
pycharm:提供集成开发环境，官网下载社区版本安装包安装即可            
可参考如下视频进行安装,【大模型应用开发基础】集成开发环境搭建Anaconda+PyCharm                         
https://www.bilibili.com/video/BV1q9HxeEEtT/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                                    
https://youtu.be/myVgyitFzrA                      

## 2.2 OneAPI安装、部署、创建渠道和令牌 
### （1）OneAPI是什么
官方介绍：是OpenAI接口的管理、分发系统             
支持 Azure、Anthropic Claude、Google PaLM 2 & Gemini、智谱 ChatGLM、百度文心一言、讯飞星火认知、阿里通义千问、360 智脑以及腾讯混元             
### (2)安装、部署
使用官方提供的release软件包进行安装部署 ，详情参考如下链接中的手动部署：                  
https://github.com/songquanpeng/one-api                  
下载OneAPI可执行文件one-api并上传到服务器中然后，执行如下命令后台运行             
nohup ./one-api --port 3000 --log-dir ./logs > output.log 2>&1 &               
运行成功后，浏览器打开如下地址进入one-api页面，默认账号密码为：root 123456                 
http://IP:3000/              
### (3)创建渠道和令牌
创建渠道：大模型类型(通义千问)、APIKey(通义千问申请的真实有效的APIKey)             
创建令牌：创建OneAPI的APIKey，后续代码中直接调用此APIKey              

## 2.3 openai使用方案            
国内无法直接访问，可以使用代理的方式，具体代理方案自己选择                   
可以参考这期视频:                
【GraphRAG最新版本0.3.0对比实战评测】使用gpt-4o-mini和qwen-plus分别构建近2万字文本知识索引+本地/全局检索对比测试                                        
https://www.bilibili.com/video/BV1maHxeYEB1/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                                        
https://youtu.be/iXfsJrXCEwA                                 

## 2.4 langsmith配置         
直接在langsmith官网设置页中申请APIKey(这里可以选择使用也可以不使用)             
https://smith.langchain.com/o/93f0b841-d320-5df9-a9a0-25be027a4c09/settings                  


# 3、项目初始化
## 3.1 下载源码
GitHub中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/PromptLangchainTest        
https://gitee.com/NanGePlus/PromptLangChainTest                        

## 3.2 构建项目
使用pycharm构建一个项目，为项目配置虚拟python环境               
项目名称：PromptLangchainTest                 

## 3.3 将相关代码拷贝到项目工程中           
直接将下载的文件夹中的文件拷贝到新建的项目目录中               

## 3.4 安装项目依赖          
pip install -r requirements.txt            
每个软件包后面都指定了本次视频测试中固定的版本号                  


# 4、项目测试          
## 4.1 基础案例:推荐流量包的智能客服测试
### （1）启动main脚本
实现使用langchain框架，模拟实现推荐流量包的智能客服                  
进入basic文件夹下，在使用python main.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                        
**调整1:设置langsmith环境变量:**           
os.environ["LANGCHAIN_TRACING_V2"] = "true"                      
os.environ["LANGCHAIN_API_KEY"] = "这里填写申请的API_KEY"                       
**调整2:prompt模版设置相关:**           
PROMPT_TEMPLATE_TXT_SYS = "prompt_template_system.txt"  # 模版文件路径                      
PROMPT_TEMPLATE_TXT_USER = "prompt_template_user.txt"  # 模版文件路径           
**调整3:选择使用哪种模型标志设置:**             
API_TYPE = "oneapi"  # openai:调用gpt模型；oneapi:调用oneapi方案支持的模型(这里调用通义千问)                              
**调整4:openai模型相关配置 根据自己的实际情况进行调整:**                  
OPENAI_API_BASE = "这里填写API调用的URL地址"                      
OPENAI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                         
OPENAI_CHAT_MODEL = "gpt-4o-mini"                               
**调整5:oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整:**              
ONEAPI_API_BASE = "这里填写oneapi调用的URL地址"                    
ONEAPI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                     
ONEAPI_CHAT_MODEL = "qwen-plus"                                     
**调整6:API服务设置相关  根据自己的实际情况进行调整:**                         
PORT = 8012  # 服务访问的端口                  
### （2）运行apiTest脚本进行检索测试             
进入basic文件夹下，在使用python apiTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数，运行成功后，可以查看smith的跟踪情况                  
**调整1:默认非流式输出 True or False**                         
stream_flag = False                      
**调整2:检查URL地址中的IP和PORT是否和main脚本中相同**                          
url = "http://localhost:8012/v1/chat/completions"      

## 4.2 基础案例:推荐流量包的智能客服测试(进阶1-短期记忆、长期记忆)
### （1）启动main脚本
实现使用langchain框架，在推荐流量包的智能客服项目的基础上增加短期记忆、长期记忆                           
进入withMemoryTest文件夹下，在使用python main.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                                  
**调整1:设置langsmith环境变量:**           
os.environ["LANGCHAIN_TRACING_V2"] = "true"                      
os.environ["LANGCHAIN_API_KEY"] = "这里填写申请的API_KEY"                       
**调整2:prompt模版设置相关:**           
PROMPT_TEMPLATE_TXT_SYS = "prompt_template_system.txt"  # 模版文件路径                      
PROMPT_TEMPLATE_TXT_USER = "prompt_template_user.txt"  # 模版文件路径           
**调整3:选择使用哪种模型标志设置:**             
API_TYPE = "oneapi"  # openai:调用gpt模型；oneapi:调用oneapi方案支持的模型(这里调用通义千问)                              
**调整4:openai模型相关配置 根据自己的实际情况进行调整:**                  
OPENAI_API_BASE = "这里填写API调用的URL地址"                      
OPENAI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                         
OPENAI_CHAT_MODEL = "gpt-4o-mini"                               
**调整5:oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整:**              
ONEAPI_API_BASE = "这里填写oneapi调用的URL地址"                    
ONEAPI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                     
ONEAPI_CHAT_MODEL = "qwen-plus"                                     
**调整6:API服务设置相关  根据自己的实际情况进行调整:**                         
PORT = 8012  # 服务访问的端口                       
### （2）运行apiTest脚本进行检索测试             
进入basic文件夹下，在使用python apiTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数，运行成功后，可以查看smith的跟踪情况                  
**调整1:默认非流式输出 True or False**                         
stream_flag = False                      
**调整2:检查URL地址中的IP和PORT是否和main脚本中相同**                          
url = "http://localhost:8012/v1/chat/completions"   

## 4.3 模拟客服质量检查测试(进阶2-思维链 Chain of Thoughts CoT)
思维链，是大模型训练中意外发现的一种推理能力，这一现象展示了人工智能在解决复杂问题时能够模仿人类思维的方式，分解问题并逐步解决，从而提高答案的准确性                                                    
它是偶然被发现的(OpenAI的人在训练时没想过会这样)                                       
有人在提问时以「Let’s think step by step」「请一步一步分析」对话开头，结果发现AI会把问题分解成多个步骤，然后逐步解决，使得输出的结果更加准确                             
思维链的原理:                        
让AI生成更多相关的内容，构成更丰富的「上文」，从而提升「下文」正确的概率                             
对涉及计算和逻辑推理等复杂问题，尤为有效                                  
人，不也是这样吗？多想一会儿，答案更靠谱。所以，得把AI当然看                              
### （1）启动main脚本               
进入cot文件夹下，在使用python main.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                        
**调整1:设置langsmith环境变量:**           
os.environ["LANGCHAIN_TRACING_V2"] = "true"                      
os.environ["LANGCHAIN_API_KEY"] = "这里填写申请的API_KEY"                       
**调整2:prompt模版设置相关:**           
PROMPT_TEMPLATE_TXT_SYS = "prompt_template_system.txt"  # 模版文件路径                      
PROMPT_TEMPLATE_TXT_USER = "prompt_template_user.txt"  # 模版文件路径           
**调整3:选择使用哪种模型标志设置:**             
API_TYPE = "oneapi"  # openai:调用gpt模型；oneapi:调用oneapi方案支持的模型(这里调用通义千问)                              
**调整4:openai模型相关配置 根据自己的实际情况进行调整:**                  
OPENAI_API_BASE = "这里填写API调用的URL地址"                      
OPENAI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                         
OPENAI_CHAT_MODEL = "gpt-4o-mini"                               
**调整5:oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整:**              
ONEAPI_API_BASE = "这里填写oneapi调用的URL地址"                    
ONEAPI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                     
ONEAPI_CHAT_MODEL = "qwen-plus"                                     
**调整6:API服务设置相关  根据自己的实际情况进行调整:**                         
PORT = 8012  # 服务访问的端口              
### （2）运行apiTest脚本进行检索测试             
进入basic文件夹下，在使用python apiTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数，运行成功后，可以查看smith的跟踪情况                  
**调整1:默认非流式输出 True or False**                         
stream_flag = False                      
**调整2:检查URL地址中的IP和PORT是否和main脚本中相同**                          
url = "http://localhost:8012/v1/chat/completions"                          

## 4.4 模拟客服质量检查测试(进阶3-自洽性 Self-Consistency)
一种对抗“幻觉”的手段。就像我们做数学题，要多次验算一样                                         
同样prompt跑多次，通过投票选出最终结果                            
### （1）启动main脚本               
进入selfConsistency文件夹下，在使用python main.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                        
**调整1:设置langsmith环境变量:**           
os.environ["LANGCHAIN_TRACING_V2"] = "true"                      
os.environ["LANGCHAIN_API_KEY"] = "这里填写申请的API_KEY"                       
**调整2:prompt模版设置相关:**           
PROMPT_TEMPLATE_TXT_SYS = "prompt_template_system.txt"  # 模版文件路径                      
PROMPT_TEMPLATE_TXT_USER = "prompt_template_user.txt"  # 模版文件路径           
**调整3:选择使用哪种模型标志设置:**             
API_TYPE = "oneapi"  # openai:调用gpt模型；oneapi:调用oneapi方案支持的模型(这里调用通义千问)                              
**调整4:openai模型相关配置 根据自己的实际情况进行调整:**                  
OPENAI_API_BASE = "这里填写API调用的URL地址"                      
OPENAI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                         
OPENAI_CHAT_MODEL = "gpt-4o-mini"                               
**调整5:oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整:**              
ONEAPI_API_BASE = "这里填写oneapi调用的URL地址"                    
ONEAPI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                     
ONEAPI_CHAT_MODEL = "qwen-plus"                                     
**调整6:API服务设置相关  根据自己的实际情况进行调整:**                         
PORT = 8012  # 服务访问的端口                
### （2）运行apiTest脚本进行检索测试             
进入basic文件夹下，在使用python apiTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数，运行成功后，可以查看smith的跟踪情况                  
**调整1:默认非流式输出 True or False**                         
stream_flag = False                      
**调整2:检查URL地址中的IP和PORT是否和main脚本中相同**                          
url = "http://localhost:8012/v1/chat/completions"                    

## 4.5 进阶案例3:指标解读、项目推荐(进阶4-思维树（Tree-of-thought, ToT）)             
是一个扩展了思维链（Chain of Thought, CoT）的方法，用于解决复杂问题的推理和规划任务                      
相比于传统的线性思维链，思维树通过采样和评估多个思维分支，以树状结构进行推理，从而更全面地探索了解空间，最终提高问题解决的准确性和效率                             
**(1)在思维链的每一步，采样多个分支**                     
在传统的思维链中，推理过程通常是线性和单一的，每一步仅选择一个推理路径                           
在思维树中，每一步的推理过程会采样多个可能的分支。每个分支代表一个可能的推理路径或选择，这样可以并行探索多个空间                        
举例：          
假设要解决一个数学问题，传统的思维链可能会按照一个固定的步骤逐步推理                      
在思维树中，系统会在每个步骤考虑多个不同的计算方法或公式，并生成多个可能的解决方案分支                      
**(2)拓扑展开成一棵思维树**                     
随着多个分支的生成，整个推理过程不再是线性的，而是拓扑展开成一棵思维树              
每个节点代表一个推理步骤，每个边代表一个推理路径，整个树结构展示了从起始状态到可能解的所有推理路径             
关键点：          
根节点：表示问题的初始状态或起始条件           
分支节点：表示每一步可能的推理选择           
叶子节点：表示最终的解决方案或推理结果              
**(3)判断每个分支的任务完成度，以便进行启发式搜索**              
由于思维树会产生多个分支，评估每个分支的完成度是关键的一步          
这意味着需要衡量每个分支在完成任务方面的潜力和进展              
基于这些评估，启发式搜索算法可以更有效地选择哪些分支应该进一步展开和探索              
**(4)设计搜索算法**                     
在构建和评估思维树的基础上，需要设计适合的搜索算法来选择最优的路径              
这些算法可以基于深度优先、广度优先、蒙特卡洛树搜索（MCTS）等策略，结合启发式评分，决定如何在思维树中进行搜索             
搜索策略：            
深度优先搜索：深入探索每一个可能的路径，直到找到一个解或达到搜索深度限制          
广度优先搜索：同时展开所有可能的路径，逐层搜索直到找到最优解            
启发式搜索：结合任务完成度和启发式评分，选择最可能成功的路径进行深入探索                
**(5)判断叶子节点的任务完成的正确性**             
当搜索算法到达思维树的叶子节点时，需要判断这些节点对应的任务是否正确完成            
这一步的目的是确保最终的解决方案确实能够满足问题的要求，并且是正确的             
方法：          
验证推理路径的逻辑一致性            
检查解决方案是否符合问题的初始条件和目标            
使用外部验证（如专家审查、模型校验）来确保任务完成的正确性                      
**案例描述:** 小明 100 米跑成绩：10.5 秒，1500 米跑成绩：3 分 20 秒，铅球成绩：12 米。他适合参加哪些搏击运动训练                                             
### （1）启动main脚本               
进入tot文件夹下，在使用python main.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                        
**调整1:设置langsmith环境变量:**           
os.environ["LANGCHAIN_TRACING_V2"] = "true"                       
os.environ["LANGCHAIN_API_KEY"] = "这里填写申请的API_KEY"                       
**调整2:prompt模版设置相关:**           
PROMPT_TEMPLATE_TXT_ANALYSER = "prompt_template_performanceAnalyser.txt"             
PROMPT_TEMPLATE_TXT_SPORTS = "prompt_template_possibleSports.txt"                 
PROMPT_TEMPLATE_TXT_EVALUATE = "prompt_template_evaluate.txt"         
PROMPT_TEMPLATE_TXT_REPORT = "prompt_template_reportGenerator.txt"                       
**调整3:选择使用哪种模型标志设置:**             
API_TYPE = "oneapi"  # openai:调用gpt模型；oneapi:调用oneapi方案支持的模型(这里调用通义千问)                              
**调整4:openai模型相关配置 根据自己的实际情况进行调整:**                  
OPENAI_API_BASE = "这里填写API调用的URL地址"                      
OPENAI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                         
OPENAI_CHAT_MODEL = "gpt-4o-mini"                               
**调整5:oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整:**              
ONEAPI_API_BASE = "这里填写oneapi调用的URL地址"                    
ONEAPI_CHAT_API_KEY = "这里填写LLM模型的API_KEY"                     
ONEAPI_CHAT_MODEL = "qwen-plus"                                     
**调整6:API服务设置相关  根据自己的实际情况进行调整:**                         
PORT = 8012  # 服务访问的端口                      
### （2）运行apiTest脚本进行检索测试             
进入basic文件夹下，在使用python apiTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数，运行成功后，可以查看smith的跟踪情况                  
**调整1:默认非流式输出 True or False**                         
stream_flag = False                      
**调整2:检查URL地址中的IP和PORT是否和main脚本中相同**                          
url = "http://localhost:8012/v1/chat/completions"  



                        
