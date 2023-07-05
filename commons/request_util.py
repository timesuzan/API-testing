# -*- coding:utf-8 -*-

import requests


class RequestUtil:
    session = requests.session()

    def send_all_request(self, **kwargs):
        res = RequestUtil.session.request(**kwargs)
        return res
