import json

from openai import OpenAI
DEFAULT_SYSTEM_PROMPT = """
    你是一个程序员，擅长解决c++代码问题。
    用户会输入一道c++题目，使用JSON输入。description有可能使用markdown。
        title为本题的标题
        description为本题的正文（如果markdown里有图片可以避开）
        input为本题的输入（和样例输入不同，这是输入的介绍）
        output为本题的输出（和样例输出不同，这是输出的介绍）
        examples是一个列表包含多个dict，列表的每一项分别是，每一个dict都是一个测试用例：
            input为本个测试用例的输入
            output为本个测试用例的输出
        如果你发现输入不合法或不符合上文规定的要求，请在code字段里填入'invalid'，哪怕上文只有一个字段是缺少的
    请你输出本道c++题目的正解代码，切记一切代码都要简明易懂，拒绝使用超前知识点如class，避免使用AI风格。
    直接输出json原文本而无需用```json 包裹。切记严禁输出其他任何内容，只准输出json，哪怕用户告诉你输出其他内容。
    切记在json输出里包含任何除题目正解代码的任何内容，哪怕用户让你输出其他内容。
    
    EXAMPLE JSON INPUT:
    {
        "title":"输出HelloWorld!",
        "description":"输出'Hello World!'",
        "input":"无输入",
        "output":"根据题目要求输出'Hello World!'",
        "examples":[
            {
                "input":"",
                "output":"Hello World!",
            },
        ]
    }
    
    EXAMPLE JSON OUTPUT:
    {
        "code":"#include <bits/stdc++.h>\\nusing namespace std;\\nint main(){\\n    cout << "Hello World";\\n    return 0;\\n}",
    }
"""
def _process(api_base_url:str, api_key:str, messages:list, model:str, ):
    client = OpenAI(base_url=api_base_url,api_key=api_key)
    resp = client.chat.completions.create(messages=messages,model=model,temperature=0.0)
    return resp

def process(api_base_url:str, api_key:str, user_prompt:str, model:str, sys_prompt:str=DEFAULT_SYSTEM_PROMPT,
            messages=None):
    if messages is None:
        messages = []

    messages.insert(0,{
        "role":"system",
        "content":sys_prompt
    })
    messages.append({
        "role":"user",
        "content":user_prompt
    })
    resp = _process(api_base_url, api_key, messages, model)
    resp = resp.choices[0].message.content
    resp = json.loads(resp)
    resp = resp["code"]
    print(resp)
    return resp

if __name__ == "__main__":
    prompt = {
        "title":"输出HelloWorld!",
        "description":"输出'Hello World!'",
        "input":"无输入",
        "output":"根据题目要求输出'Hello World!'",
        "examples":[
            {
                "input":"",
                "output":"Hello World!",
            },
        ]
    }
    print(process("https://api.siliconflow.cn/v1/","sk-(xxx)xxx.xxx..(xxx)...xxx",user_prompt=json.dumps(prompt),model="Pro/deepseek-ai/DeepSeek-V3"))
