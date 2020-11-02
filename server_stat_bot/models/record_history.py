# coding=utf-8

from guniflask.orm import BaseModelMixin
from sqlalchemy.dialects.mysql.types import DATETIME
from sqlalchemy.dialects.mysql.types import INTEGER
from sqlalchemy.dialects.mysql.types import VARCHAR

from server_stat_bot import db


class RecordHistory(BaseModelMixin, db.Model):
    __tablename__ = 'record_history'

    id = db.Column(INTEGER, primary_key=True, autoincrement=True)
    server_address = db.Column(VARCHAR(256), nullable=False)
    server_stat_code = db.Column('serverStatCode', VARCHAR(10))
    fetch_time = db.Column('fetchTime', DATETIME, nullable=False)
    remark = db.Column(VARCHAR(512))
    dingtalk_resp_stat_code = db.Column('dingtalkRespStatCode', VARCHAR(10), nullable=False)
    dingtalk_resp_text = db.Column('dingtalkRespText', VARCHAR(1024), nullable=False)
