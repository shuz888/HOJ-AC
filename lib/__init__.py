import json

import requests

from lib.submit_code import submit
from lib.get_problem import get_problem_detail
from lib.ai_process import process

def together(base_url: str,pid: str,api_base_url: str,api_key: str,model: str,session: requests.Session):
    problem_data = get_problem_detail(pid=pid,base_url=base_url)
    code = process(api_base_url=api_base_url,api_key=api_key,model=model,user_prompt=json.dumps(problem_data))
    submit(base_url,pid,code,session)

if __name__ == '__main__':
    pass