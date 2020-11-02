# coding=utf-8
from guniflask.scheduling import scheduled
from guniflask.web import blueprint
from guniflask.config import settings
import datetime
import requests

from server_stat_bot import db
from server_stat_bot.models import record_history
from server_stat_bot.unit.trans_server_msg import transServerMsg2Md
from server_stat_bot.unit.dingtalk_webhook import markdown_json


@blueprint('/api')
class CornController:
    @scheduled(interval=int(settings['configYaml']['CYCLE_FETCH_TIME_MIN'] * 60))
    def schedule_corn_request(self):
        # TODO util task request
        serverMsgs = []
        for serverUrl in settings['configYaml']['DES_WEB_LIST']:
            serverMsg = {'url': serverUrl, 'status_code': None, 'local_time': datetime.datetime.now()}
            try:
                resp = requests.get(url=serverUrl)
                serverMsg['status_code'] = resp.status_code
            except Exception as e:
                print(e)
                pass
            serverMsgs.append(serverMsg)

        # use Md to post
        mdText = transServerMsg2Md(serverMsgs)

        postJson = markdown_json(title=settings['configYaml']['DINGTALK_TITLE'], mdText=mdText,
                                 isAtAll=settings['configYaml']['DINGTALK_AT_ALL'])
        header = {
            'Content-Type': 'application/json'
        }
        dingtalkRespStatCode = None
        dingtalkRespText = ''
        try:
            resp = requests.post(url=settings['configYaml']['DINGTALK_WEBHOOK_URL'], headers=header, json=postJson)
            dingtalkRespStatCode = resp.status_code
            dingtalkRespText = resp.text
        except Exception as e:
            print(e)
            pass

        for serverMsg in serverMsgs:
            recordHistory = record_history.RecordHistory()
            recordHistory.server_address = serverMsg['url']
            recordHistory.fetch_time = serverMsg['local_time'].strftime('%Y-%m-%d %H:%M:%S')
            recordHistory.server_stat_code = serverMsg['status_code']
            recordHistory.dingtalk_resp_stat_code = dingtalkRespStatCode
            recordHistory.dingtalk_resp_text = dingtalkRespText
            db.session.add(recordHistory)
        db.session.commit()
