from urllib.parse import urljoin

import requests

import re
from typing import List, Dict

# by deepseek
def convert_io_to_list(text: str) -> List[Dict[str, str]]:
    """
    将特定格式的输入输出转换为[{"input":xxx,"output":xxx},...]格式

    Args:
        text: 包含<input>和<output>标签的字符串

    Returns:
        转换后的字典列表
    """
    # 使用正则表达式匹配所有<input>和<output>标签内容
    input_matches = re.findall(r'<input>(.*?)</input>', text, re.DOTALL)
    output_matches = re.findall(r'<output>(.*?)</output>', text, re.DOTALL)

    # 检查输入输出数量是否匹配
    if len(input_matches) != len(output_matches):
        raise ValueError("输入和输出的数量不匹配")

    # 构建结果列表
    result = []
    for i in range(len(input_matches)):
        result.append({
            "input": input_matches[i].strip(),
            "output": output_matches[i].strip()
        })

    return result

def _get_problem_detail(pid:str, url:str):
    url = urljoin(url,"?problemId="+pid)
    return requests.get(url)

def get_problem_detail(pid:str, base_url:str):
    url = urljoin(base_url, "/api/get-problem-detail/")
    resp = _get_problem_detail(pid,url)
    print(resp.text)
    if(resp.status_code!=200):
        return None
    resp = resp.json()
    examples = convert_io_to_list(resp["data"]["problem"]["examples"])

    res = {
        "title":resp["data"]["problem"]["title"],
        "description":resp["data"]["problem"]["description"],
        "input":resp["data"]["problem"]["input"],
        "output":resp["data"]["problem"]["output"],
        "examples":examples
    }
    return res

if __name__ == '__main__':
    print(get_problem_detail("A1001","http://www.algo-code.cn"))