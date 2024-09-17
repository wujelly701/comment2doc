# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : parsing_error.py
@ Time       ：2024/9/14 1:30
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
from .base_exception import LuaDocGeneratorError

class ParsingError(LuaDocGeneratorError):
    """解析错误，用于 Lua 代码解析过程中的问题"""
    pass