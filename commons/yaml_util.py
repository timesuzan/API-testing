# -*- coding:utf-8 -*-
import os

import yaml


def read_yaml_testcase(path):
    with open(path, encoding="UTF-8", mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


def write_yaml(data):
    with open(os.getcwd() + "/extract.yaml", encoding="UTF-8", mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def read_yaml():
    with open(os.getcwd() + "/extract.yaml", encoding="UTF-8", mode="r") as f:
        return yaml.load(f, yaml.FullLoader)

def clear_yaml():
    with open(os.getcwd() + "/extract.yaml", encoding="UTF-8", mode="w") as f:
        f.truncate()
