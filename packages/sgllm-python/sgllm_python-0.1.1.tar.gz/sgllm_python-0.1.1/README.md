# SGLLM大模型接入库(sgllm-python)

## 快速开始

SGLLM大模型 SDK 提供基于 HTTP 的 API 服务接入，并且大部分 API 兼容了 OpenAI。

## 安装

```bash
pip install --upgrade 'sgllm-python>=0.1'
```

## 使用

### 单轮对话

```python
from sgllm import SGLLM
 
client = SGLLM(
    api_key="$API_KEY",                           # $API_KEY 需要替换为您在平台上创建的 API Key
    base_url="https://api-sgllm.sgccnlp.com/v1",  # 替换模型访问地址
)
 
completion = client.chat.completions.create(
    model="SGLLM-34B-Chat-4bits",
    messages=[
        {"role": "system", "content": "你是由智研院提供的人工智能助手，你更擅长电力行业领域知识。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。"},
        {"role": "user", "content": "变压器故障种类有哪些？"}
    ],
    temperature=0.3,
    stream=True
)
 
print(completion.choices[0].message.content)
```

### 多轮对话

```python
from sgllm import SGLLM

client = SGLLM(
    api_key="$API_KEY",                            # $API_KEY 需要替换为您在平台上创建的 API Key
    base_url="https://api-sgllm.sgccnlp.com/v1",   # 替换模型访问地址
)
 
history = [
    {"role": "system", "content": "你是由智研院提供的人工智能助手，你更擅长电力行业领域知识。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。"}
]
 
def chat(query, history):
    history.append([{
        "role": "user", 
        "content": query
    }])
    completion = client.chat.completions.create(
        model="SGLLM-Chat-4bits",
        messages=history,
        temperature=0.3,
        stream=True
    )
    result = completion.choices[0].message.content
    history.append([{
        "role": "assistant",
        "content": result
    }])
    return result
 
print(chat("变压器故障种类有哪些？", history))
print(chat("变压器套管破损如何处理？", history))
```

### 响应示例

该接口将以 Event-Stream 格式返回数据，调用方需要拼接每次增量产生的生成内容。

```txt
HTTP
data: {"id": "message-id","model":"SGLLM-34B-Chat-4bits","object":"chat.completion.chunk"，"created": 1715145112, "choices": [{"index": 0, "delta": {"content": " 虚拟",  "role":"assistant"}, "finish_reason": null}]}

data: {"id": "message-id","model":"SGLLM-34B-Chat-4bits","object":"chat.completion.chunk"，"created": 1715145112, "choices": [{"index": 0, "delta": {"content": "助手",  "role":"assistant"}, "finish_reason": null}]}

data: {"id": "message-id","model":"SGLLM-34B-Chat-4bits", "object":"chat.completion.chunk"，"created": 1715145112, "choices": [{"index": 0, "delta": {"content": "。",  "role":"assistant"}, "finish_reason": null}]}

data: {"id": "message-id","model":"SGLLM-34B-Chat-4bits", "object":"chat.completion.chunk"，"created": 1715145112, "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]}

data: [DONE]
```