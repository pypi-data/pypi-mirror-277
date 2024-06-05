# SGLLM大模型接入库(sgllm-python)

## 快速开始

SGLLM大模型 SDK 提供基于 HTTP 的 API 服务接入，并且大部分 API 兼容了 OpenAI。

## 安装

```bash
pip install --upgrade 'sgllm-python'
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
    stream=True     # 启用流式响应
)

# 非流式: stream=False
print(completion.choices[0].message.content)
 
# 流式  : stream=True
for chunk in completion:
    print(completion.choices[0].delta.content)
```

### 多轮对话

```python
from sgllm import SGLLM

client = SGLLM(
    api_key="$API_KEY",                            # $API_KEY 需要替换为您在平台上创建的 API Key
    base_url="https://api-sgllm.sgccnlp.com/v1",   # 替换模型访问地址
)
 
history = [
    {"role": "system", "content": "你是由SGLLM提供的人工智能助手，你更擅长电力行业领域知识。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。"}
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

### 非流式

该接口会一次返回完整答案，但需等待较长时间

```json
{
  "id": "cmpl-d6ddf1e87b70492e916c8e3229728bda",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "变压器故障种类主要包括以下几种：\n\n1. 短路故障：这是最常见的变压器故障类型之一，通常由外部因素引起，如雷击、设备绝缘老化、动物侵袭等。短路故障会导致变压器绕组温度急剧上升，甚至可能引发火灾。\n\n2. 接地故障：当变压器绕组或金属部件与大地之间出现非正常连接时，就会发生接地故障。这种故障可能导致变压器绕组绝缘损坏，甚至引发触电危险。\n\n3. 过载故障：当变压器长时间超过其额定容量运行时，可能会导致过热和绝缘损坏，从而引发故障。\n\n4. 冷却系统故障：变压器的冷却系统出现问题，如冷却器故障或冷却介质泄漏，可能导致变压器温度过高，进而引发故障。\n\n5. 绝缘故障：变压器绝缘材料因老化、受潮或受到电、热、机械损伤而导致的故障。\n\n6. 分接开关故障：变压器分接开关是用来调节输出电压的，如果分接开关接触不良或损坏，可能会导致变压器故障。\n\n7. 铁芯故障：变压器铁芯因局部过热、涡流效应或铁芯叠片松动等原因导致的故障。\n\n8. 油系统故障：对于油浸式变压器，油系统问题如渗漏、油位过高或过低、油温异常等都可能导致故障。\n\n9. 振动和噪声故障：变压器运行时产生的异常振动和噪声可能是故障的迹象，如绕组松动、铁芯变形等。\n\n10. 外部环境影响：如温度过高、湿度过大、灰尘过多等外部环境因素也可能导致变压器故障。\n\n为了防止这些故障的发生，需要定期对变压器进行维护和检查，包括外观检查、绝缘测试、温度监测、冷却系统检查等。同时，及时处理发现的异常情况，以延长变压器的使用寿命并确保其安全运行。",
        "role": "assistant"
      }
    }
  ],
  "created": 2279230,
  "model": "SGLLM-34B-Chat-4bits",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 416,
    "prompt_tokens": 68,
    "total_tokens": 484
  }
}
```

#### 流式

该接口将以 Event-Stream 格式返回数据，调用方需要拼接每次增量产生的生成内容。

```txt
HTTP
data: {"id": "message-id","model":"SGLLM-34B-Chat-4bits","object":"chat.completion.chunk"，"created": 1715145112, "choices": [{"index": 0, "delta": {"content": " 虚拟",  "role":"assistant"}, "finish_reason": null}]}

data: {"id": "message-id","model":"SGLLM-34B-Chat-4bits","object":"chat.completion.chunk"，"created": 1715145112, "choices": [{"index": 0, "delta": {"content": "助手",  "role":"assistant"}, "finish_reason": null}]}

data: {"id": "message-id","model":"SGLLM-34B-Chat-4bits", "object":"chat.completion.chunk"，"created": 1715145112, "choices": [{"index": 0, "delta": {"content": "。",  "role":"assistant"}, "finish_reason": null}]}

data: {"id": "message-id","model":"SGLLM-34B-Chat-4bits", "object":"chat.completion.chunk"，"created": 1715145112, "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]}

data: [DONE]
```
