import pytest
from commons.yaml_util import *
from commons.request_util import RequestUtil
import jsonpath

class TestCreateAccount:

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("config/test_create_account.yaml"))
    def test_create_account(self, accountinfo):
        #print(accountinfo)
        method = accountinfo["request"]["method"]
        url = accountinfo["request"]["url"]
        headers = accountinfo["request"]["Authentication"]
        data = accountinfo["request"]["body"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers, data=data)
        account_id = (jsonpath.jsonpath(res.json(), "$.id")[0])
        write_yaml({"insert_account_id": account_id})
        assert res.status_code == 201

    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("config/test_create_account.yaml"))
    def test_create_account_without_body(self, accountinfo):
        # print(accountinfo)
        method = accountinfo["request"]["method"]
        url = accountinfo["request"]["url"]
        headers = accountinfo["request"]["Authentication"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers)
        # print(res.json())
        assert res.status_code == 400

    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("config/test_create_account.yaml"))
    def test_create_account_without_headers(self, accountinfo):
        # print(accountinfo)
        method = accountinfo["request"]["method"]
        url = accountinfo["request"]["url"]
        data = accountinfo["request"]["body"]
        res = RequestUtil().send_all_request(method=method, url=url, data=data)
        # print(res.json())
        assert res.status_code == 401

    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("config/test_create_account.yaml"))
    def test_create_account_body_with_gender(self, accountinfo):
        # print(accountinfo)
        method = accountinfo["request"]["method"]
        url = accountinfo["request"]["url"]
        headers = accountinfo["request"]["Authentication"]
        data = accountinfo["request"]["body_add_gender"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers, data=data)
        # print(res.json())
        assert res.status_code == 201

    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("config/test_create_account.yaml"))
    def test_create_account_body_without_type(self, accountinfo):
        # print(accountinfo)
        method = accountinfo["request"]["method"]
        url = accountinfo["request"]["url"]
        headers = accountinfo["request"]["Authentication"]
        data = accountinfo["request"]["body_without_type"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers, data=data)
        # print(res.json())
        assert res.status_code == 400