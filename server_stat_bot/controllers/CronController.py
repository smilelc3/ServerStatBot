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
import logging

log = logging.getLogger(__name__)

@blueprint('/cron')
class CornController:
    @scheduled(initial_delay=settings['FETCH_TIME_MIN_PLAN'] * 60)
    def schedule_corn_request(self):
        serverMsgs = []
        for serverUrl in settings['configYaml']['DES_WEB_LIST']:
            serverMsg = {'url': serverUrl, 'status_code': None, 'local_time': datetime.datetime.now(), 'remark': ''}
            try:
                resp = requests.get(url=serverUrl)
                serverMsg['status_code'] = resp.status_code
            except Exception as e:
                log.warning(e)
                serverMsg['remark'] = str(e)
                pass
            serverMsgs.append(serverMsg)

        # use Md to post
        mdText = transServerMsg2Md(serverMsgs)

        postJson = markdown_json(title=settings['DINGTALK_TITLE'], mdText=mdText,
                                 isAtAll=settings['DINGTALK_AT_ALL'])
        header = {
            'Content-Type': 'application/json'
        }
        dingtalkRespStatCode = ''
        dingtalkRespText = ''
        try:
            resp = requests.post(url=settings['DINGTALK_WEBHOOK_URL'], headers=header, json=postJson)
            dingtalkRespStatCode = resp.status_code
            dingtalkRespText = resp.text
        except Exception as e:
            log.warning(e)
            pass

        for serverMsg in serverMsgs:
            recordHistory = record_history.RecordHistory()
            recordHistory.server_address = serverMsg['url']
            recordHistory.fetch_time = serverMsg['local_time'].strftime('%Y-%m-%d %H:%M:%S')
            recordHistory.server_stat_code = serverMsg['status_code']
            recordHistory.remark = serverMsg['remark']
            recordHistory.dingtalk_resp_stat_code = dingtalkRespStatCode
            recordHistory.dingtalk_resp_text = dingtalkRespText
            db.session.add(recordHistory)
        db.session.commit()


