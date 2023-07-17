# -*- coding:utf-8 -*-
import pytest
from commons.yaml_util import *
from commons.request_util import RequestUtil
import jsonpath


class TestAccountList:

    @pytest.mark.run(order=0)
    @pytest.mark.parametrize("accountinfo", read_yaml_testcase("../config/test_account_list.yaml"))
    def test_account_list(self, accountinfo):
        #print(accountinfo)
        method = accountinfo["request"]["method"]
        url = accountinfo["request"]["url"]
        res = RequestUtil().send_all_request(method=method, url=url)
        #print(res.json())
        account_id = (jsonpath.jsonpath(res.json(), "$.data.customers")[0][2].get('id'))
        write_yaml({"account_id": account_id
                    })
        assert res.status_code == 200
