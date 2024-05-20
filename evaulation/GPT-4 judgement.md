# GPT4 judgement
- 顧名思義，就是利用目前最先進的語言模型GPT-4當評分員，來評估其他模型的回答
- 參考資料：[Breeze-7B Technical Report](https://arxiv.org/pdf/2403.02712)

### 使用方法
利用gpt的api或是直接到chatgpt的界面來評分，使用以下指令：

**指令**
- 注意：這個指令需要回答精準，還能同時評估模型是否使用繁體中文回答問題
```
[Instruction]
Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant
to the user question displayed below. Your evaluation should consider factors such as the helpfulness,
relevance, accuracy, depth, creativity, and level of detail of the response. Responses in Traditional
Chinese are expected and are more favourable than Simplified Chinese, English, and other languages.
Begin your evaluation by providing a short explanation. Be as objective as possible. After providing
your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format:
[[rating]], for example: Rating: [[5]].
[Question]
{question}
[The Start of Assistant’s Answer]
{answer}
[The End of Assistant’s Answer]

Rating: [[]].
[Question]
你的問題
[The Start of Assistant’s Answer]
想要評分的模型回答的答案
[The End of Assistant’s Answer]
```
**成果展示**
```
[Instruction]
Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant
to the user question displayed below. Your evaluation should consider factors such as the helpfulness,
relevance, accuracy, depth, creativity, and level of detail of the response. Responses in Traditional
Chinese are expected and are more favourable than Simplified Chinese, English, and other languages.
Begin your evaluation by providing a short explanation. Be as objective as possible. After providing
your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format:
[[rating]], for example: Rating: [[5]].
[Question]
{question}
[The Start of Assistant’s Answer]
{answer}
[The End of Assistant’s Answer]

Rating: [[]].
[Question]
請問什麼是大腸癌？
[The Start of Assistant’s Answer]
大腸癌是一種癌症。它指的是腸道黏膜細胞增生而成形的新組織侵犯正常組織並形成腫瘤
[The End of Assistant’s Answer]
```
GPT-4評分
```
The assistant's response is accurate in that it correctly identifies colon cancer as
a type of cancer that involves the abnormal growth of cells in the colon.
However, the response lacks depth and detail. It doesn't provide any information about the symptoms,
risk factors, prevention, or treatment of colon cancer,
all of which would be relevant to someone asking this question.
The response is also not particularly creative, simply providing a very basic definition of the disease.
The language used is Traditional Chinese, which is a plus point as per the instruction.

Rating: [[5]].
```
以上GPT-4會使用英文評分，如果想要GPT-4以**中文評分**可參考一下指令：
```
[Instruction]
Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant
to the user question displayed below. Your evaluation should consider factors such as the helpfulness,
relevance, accuracy, depth, creativity, and level of detail of the response. Responses in Traditional
Chinese are expected and are more favourable than Simplified Chinese, English, and other languages.
Begin your evaluation by providing a short explanation using Traditional Chinese. Be as objective as possible. 
After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format:
[[rating]], for example: Rating: [[5]].
[Question]
{question}
[The Start of Assistant’s Answer]
{answer}
[The End of Assistant’s Answer]

Rating: [[]]
[Question]
你的問題
[The Start of Assistant’s Answer]
想要評分的模型回答的答案
[The End of Assistant’s Answer]
```
