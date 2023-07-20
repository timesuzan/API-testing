import pytest
from commons.yaml_util import *
from commons.request_util import RequestUtil
import jsonpath

class TestChangeAccount:

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("findaccount", read_yaml_testcase("config/test_put_account.yaml"))
    def test_change_account(self,findaccount):
        method = findaccount["request"]["method"]
        url = findaccount["request"]["url"]
        headers = findaccount["request"]["Authentication"]
        data = findaccount["request"]["body"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers, data=data)
        assert res.status_code == 200

    @pytest.mark.parametrize("findaccount", read_yaml_testcase("config/test_put_account.yaml"))
    def test_no_authorized_account(self, findaccount):
        method = findaccount["request"]["method"]
        url = findaccount["request"]["url"]
        data = findaccount["request"]["body"]
        res = RequestUtil().send_all_request(method=method, url=url, data=data)
        assert res.status_code == 401

    @pytest.mark.parametrize("findaccount", read_yaml_testcase("config/test_put_account.yaml"))
    def test_change_no_id_account(self,findaccount):
        method = findaccount["request"]["method"]
        url = "https://3x5m5o-3000.csb.app/customer/600"
        data = findaccount["request"]["body"]
        headers = findaccount["request"]["Authentication"]
        res = RequestUtil().send_all_request(method=method, url=url,  data=data, headers=headers)
        assert res.status_code == 400

    @pytest.mark.parametrize("findaccount", read_yaml_testcase("config/test_put_account.yaml"))
    def test_change_no_data_account(self, findaccount):
        method = findaccount["request"]["method"]
        url = findaccount["request"]["url"]
        headers = findaccount["request"]["Authentication"]
        res = RequestUtil().send_all_request(method=method, url=url,  headers=headers)
        assert res.status_code == 400
