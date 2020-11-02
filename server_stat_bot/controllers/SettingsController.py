# coding=utf-8

from guniflask.config import settings
from guniflask.web import blueprint, get_route


@blueprint('/api')
class SettingsController:
    @get_route('/settings/<name>')
    def get_setting(self, name):
        return str(settings[name])
