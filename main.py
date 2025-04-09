import requests
from lib import together


def main():
    s=requests.Session()
    jssid = input("请输入JSESSIONID:")
    token = input("请输入token:")
    s.cookies.update({"JSESSIONID":jssid})
    s.headers.update({"token":token})
    bsurl = input("请输入Base_url:")
    api_bsurl = input("请输入API_BASE_URL:")
    api_key = input("请输入API_KEY:")
    model = input("请输入model:")
    while True:
        pid = input("请输入pid:")
        together(bsurl,pid,api_bsurl,api_key,model,s)


if __name__ == "__main__":
    main()