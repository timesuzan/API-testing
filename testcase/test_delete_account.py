import pytest
from commons.yaml_util import *
from commons.request_util import RequestUtil
import jsonpath

class TestDeleteAccount:

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("config/test_delete_account.yaml"))
    def test_delete_account(self, accountinfo):
        #print(accountinfo)
        method = accountinfo["request"]["method"]
        id = read_yaml().get("insert_account_id")
        url = accountinfo["request"]["url"]+str(id)
        headers = accountinfo["request"]["Authentication"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers)
        #print(res.json())
        assert res.status_code == 200

    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("config/test_delete_account.yaml"))
    def test_delete_account_without_id(self, accountinfo):
        # print(accountinfo)
        method = accountinfo["request"]["method"]
        url = accountinfo["request"]["url"]
        headers = accountinfo["request"]["Authentication"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers)
        # print(res.json())
        assert res.status_code == 401

    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("config/test_delete_account.yaml"))
    def test_delete_account_with_wrong_id(self, accountinfo):
        # print(accountinfo)
        method = accountinfo["request"]["method"]
        wrong_id = 3
        url = accountinfo["request"]["url"]+str(wrong_id)
        headers = accountinfo["request"]["Authentication"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers)
        # print(res.json())
        assert res.status_code == 400