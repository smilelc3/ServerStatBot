# coding=utf-8
import yaml
configYaml = yaml.load(open('conf/app.yml', 'r'), Loader=yaml.FullLoader)

# Database URI when using Flask-SQLAlchemy, example: mysql+pymysql://username:password@server/db?charset=utf8mb4
SQLALCHEMY_DATABASE_URI = configYaml['SQLALCHEMY_DATABASE_URI']

SQLALCHEMY_TRACK_MODIFICATIONS = False

# guniflask configuration
guniflask = dict(
    cors=True,
)
