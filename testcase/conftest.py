# -*- coding:utf-8 -*-
import os

import pytest
from commons.yaml_util import clear_yaml

@pytest.fixture(scope="session", autouse=True)
def fix_ture():
    print("\n-------function-------start------")
    clear_yaml()
    yield
    print("\n-------end------")
