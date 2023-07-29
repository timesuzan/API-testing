# -*- coding:utf-8 -*-
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-q', 'testcase','--alluredir=./reports/allure-results'])
    project_root = os.getcwd()
    os.system(r"allure generate ./reports/allure-results -o ./reports/index.html --clean")

