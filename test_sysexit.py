# -*- coding: utf-8 -*-
# @Time    : 2019-8-29 11:46
# @Author  : zq
# @File    : test_sysexit.py

import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
