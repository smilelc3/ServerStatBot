# coding=utf-8
import yaml
configYaml = yaml.load(open('conf/app.yml', 'r'), Loader=yaml.FullLoader)

# Database URI when using Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/test?charset=UTF8MB4"

# Dingtalk webhook url
#DINGTALK_WEBHOOK_URL = "http://fill_your_dingtalk_webhook_url"

DINGTALK_WEBHOOK_URL = 'https://oapi.dingtalk.com/robot/send?access_token=1cc4cb4cdda998ecc50d4b6f2a12cba311766743506d0ef251e09da3321ff775'
# dingtalk msg title
DINGTALK_TITLE = "服务器健康报警"

# whether Dingtalk bot at all users
DINGTALK_AT_ALL = False

SQLALCHEMY_TRACK_MODIFICATIONS = False


# time(min) to how frequency to refresh
FETCH_TIME_MIN_PLAN = 5

# guniflask configuration
guniflask = dict(
    cors=True,
)
