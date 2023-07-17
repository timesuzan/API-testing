import pytest
from commons.yaml_util import *
from commons.request_util import RequestUtil
import jsonpath

class TestAccountList:

    @pytest.mark.run(order=0)
    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("../config/test_create_account.yaml"))
    def test_create_account(self, accountinfo):
        #print(accountinfo)
        method = accountinfo["request"]["method"]
        url = accountinfo["request"]["url"]
        headers = accountinfo["request"]["Authentication"]
        data = accountinfo["request"]["body"]
        res = RequestUtil().send_all_request(method=method, url=url, headers=headers, data=data)
        #print(res.json())
        assert res.status_code == 201