# coding=utf-8

from guniflask.context import configuration
from guniflask.security_config import enable_web_security, WebSecurityConfigurer, HttpSecurity


@configuration
@enable_web_security
class SecurityConfiguration(WebSecurityConfigurer):

    def configure_http(self, http: HttpSecurity):
        """Configure http security here"""
