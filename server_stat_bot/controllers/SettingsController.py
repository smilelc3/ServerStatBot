# coding=utf-8

from guniflask.config import settings
from guniflask.web import blueprint, get_route
from flask.json import jsonify


# SettingsController class show ALL config via web
@blueprint('/settings')
class SettingsController:
    @get_route('/')
    def show_settings(self):
        return jsonify({key: str(val) for key, val in settings.items()})

    @get_route('/<name>')
    def get_setting(self, name):
        return str(settings[name])