# coding=utf-8
import json

def base_json()-> dict:
    base = {
        "msgtype": "",
        "at": {
            "isAtAll": False
        }
    }
    return base


def markdown_json(title: str, isAtAll:bool, mdText: str) -> dict:
    mdJson = base_json()
    mdJson['msgtype'] = 'markdown'
    mdJson['markdown'] = {
        "title": str(title),
        "text": str(mdText)
    }
    mdJson['at']['isAtAll'] = isAtAll

    return mdJson

if __name__ == '__main__':
    print(type(base_json()))