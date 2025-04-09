import json
from urllib.parse import urljoin

import requests


def _submit(url:str, code_data:str, session:requests.Session):
    resp = session.post(url,data=code_data,headers={'Content-Type': 'application/json'})
    return resp

def submit(base_url:str, pid:str, code:str, session:requests.Session, language:str="C++", isRemote:int=0):
    code_data = {
        "pid": pid,
        "language": language,
        "code": code,
        "isRemote": isRemote,
    }
    code_data=json.dumps(code_data)
    resp = _submit(urljoin(base_url, "/api/submit-problem-judge"),code_data,session)
    print(resp.text)
    if(resp.status_code!=200):
        return None
    return resp.json()