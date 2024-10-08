# 1、26条有效的提示词技巧
## 1.1 论文地址
**论文名称:**                         
《Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4》                                                        
**论文PDF下载地址:**                                   
https://arxiv.org/pdf/2312.16171                             

## 1.2 具体内容
**总结下来就是26条有效的提示词技巧:**                  
**核心心法:把AI当人看**              
**核心围绕:指令具体、信息丰富、尽量少歧义**               
(1)与大模型交流无需使用礼貌用语，如“请”、“谢谢”等，直接表达需求即可                                

(2)在提示中指明目标受众，比如说受众是该领域的专家                                  

(3)把复杂任务拆解成一系列简单的提示，以进行交互式对话                               

(4)使用肯定的指令词，如“执行”，避免使用否定词汇，如“不要”                                 

(5)当你需要更清晰地理解某个主题、观点或任何信息时，可以尝试使用以下提示方式:                                   
   简单地解释一下XXX具体主题                 
   像对11岁的孩子一样向我解释                   
   像对一个XXX领域新手一样向我解释                   
   用浅显易懂的语言写作文章/文本/段落，就像是在向一个5岁孩子解释                                         

(6)添加“我愿意支付¥xxx的小费以获得更好的方案！”                  

(7)采用示例驱动的提示方式（使用少样本提示法）               

(8)格式化提示时，先写上‘#undefined#’，然后根据需要添加‘#undefined#’或‘#undefined#’。接着展示你的内容，用一行或多行空行分隔各个部分，包括指令、示例、问题、背景和输入数据                     

(9)使用这样的短语：“你的任务是”和“必须完成”         

(10)使用这样的短语：“将会受到处罚”           

(11)使用“以自然且类似人类的方式回答问题”作为你的提示             

(12)使用引导性的词汇，比如“逐步思考”           

(13)在提示中加入“确保你的回答无偏见，不依赖于刻板印象”           

(14)让大模型通过向你提问来澄清具体的细节和需求，直到它获取足够的信息来提供所需的输出，例如：“从现在开始，请向我提出问题以便......”          

(15)当你想要学习特定的主题或概念，并测试自己的理解时，可以使用这样的短语：“教我某个定理/主题/规则，在教学结束时包含一个测验，但不要直接告诉我答案。等我回答后再告诉我是否正确”            

(16)为大模型指定一个特定角色             

(17)使用明确的分隔符           

(18)在一个提示中重复特定单词或短语多次              

(19)结合思维链路 (Chain-of-thought，CoT) 和少样本提示的方法           

(20)使用输出引导符，即在提示的末尾加上期望回答的开头。这样做可以引导输出内容的方向              

(21)撰写一篇详细的论文/文本/段落/文章时，可以这样指示：“请为我详细写一篇关于XXX主题的论文/文本/段落，并添加所有必要的信息”           

(22)当需要修改特定文本但不改变其风格时，可以这样指示：“尝试修改用户提交的每个段落。你应当只改进语法和词汇，确保文本听起来自然，但不要改变其原有的写作风格，如将正式文体变为非正式文体”          

(23)面对可能涉及多个文件的复杂编程任务时，可以这样提示：“从现在开始，每当你生成涉及多个文件的代码时，创建一个某编程语言(python)脚本，自动创建所需文件或修改现有文件以插入生成的代码。描述你的问题”         

(24)当你想用特定的词汇、短语或句子开始或继续一段文本时，可以这样提示：“我为你提供了开头歌词/故事/段落/论文...：插入的词句。请根据这些词句继续写下去，保持内容的连贯性”                

(25)明确说明大模型在生成内容时必须遵循的要求，可以是关键词、规则、提示或指示               

(26)撰写任何类型的文本，如论文或段落，且想要其与提供的样本风格相似时，可以这样指示：“请根据提供的段落/标题/文本/论文/答案的风格撰写”               