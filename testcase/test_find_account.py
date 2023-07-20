# -*- coding:utf-8 -*-
import os
import pytest
import requests

from commons.request_util import RequestUtil
from commons.yaml_util import *


class TestFindAccunt:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("findaccount", read_yaml_testcase("config/test_find_account.yaml"))
    def test_find_account(self, findaccount):
        method = findaccount["request"]["method"]
        id = read_yaml().get("account_id")
        url = findaccount["request"]["url"]
        res = RequestUtil().send_all_request(method=method, url=url, params={"id": id})
        # print(res.json())
        #print(url)
        assert res.status_code == 200

    @pytest.mark.parametrize("findaccount", read_yaml_testcase("config/test_find_account.yaml"))
    def test_find_error_id_account(self, findaccount):
        method = findaccount["request"]["method"]
        error_id = -1
        url = findaccount["request"]["url"]
        res = RequestUtil().send_all_request(method=method, url=url, params={"id": error_id})
        assert res.status_code == 404

    @pytest.mark.parametrize("findaccount", read_yaml_testcase("config/test_find_account.yaml"))
    def test_find_no_id_account(self, findaccount):
        method = findaccount["request"]["method"]
        url = findaccount["request"]["url"]
        res = RequestUtil().send_all_request(method=method, url=url)
        assert res.status_code == 404

    @pytest.mark.parametrize("findaccount", read_yaml_testcase("config/test_find_account.yaml"))
    def test_find_error_params_account(self, findaccount):
        method = findaccount["request"]["method"]
        url = findaccount["request"]["url"]
        name="Blanche Devereux"
        res = RequestUtil().send_all_request(method=method, url=url, params={"name": name})
        assert res.status_code == 404