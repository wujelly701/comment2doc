# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : config_error.py
@ Time       ：2024/9/14 1:30
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
from .base_exception import LuaDocGeneratorError

class ConfigurationError(LuaDocGeneratorError):
    """配置错误，用于无效的配置选项或格式"""
    pass