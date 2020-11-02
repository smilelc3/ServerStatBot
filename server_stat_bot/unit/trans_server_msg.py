# coding=utf-8
from typing import List, Dict
import datetime


def transServerMsg2Md(serverMsgs: List[Dict]) -> str:
    # each server carry on Msg: url, statu_code, local_time
    Md = '### 服务器健康报警\n' + \
    '![warning](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1004059102,1926677534&fm=26&gp=0.jpg)\n' + \
    '\n'
    for index, serverMsg in  enumerate(serverMsgs):
        assert type(serverMsg['local_time']) == datetime.datetime
        Md = Md + f'### {index + 1}. '
        if serverMsg['status_code'] != 200:
            Md = Md + f"❗异常[{serverMsg['url']}]({serverMsg['url']})\n"
        else:
            Md = Md + f"✅正常[{serverMsg['url']}]({serverMsg['url']})\n"
        Md = Md + f"> 状态码：**{serverMsg['status_code']}**  \n"
        Md = Md + f"> 时间：**{serverMsg['local_time'].strftime('%Y-%m-%d %H:%M:%S')}**  \n"
    return Md

def transServerMsg2Text(serverMsgs: List[Dict]) -> str:
    text = "服务器健康报警\n"
    for index, serverMsg in enumerate(serverMsgs):
        text = text + f"{serverMsg['url']}\n" \
                      f"状态码：{serverMsg['status_code']}\n" \
                      f"时间：{serverMsg['local_time'].strftime('%Y-%m-%d %H:%M:%S')}\n" \
                      f"\n"
    return text