# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : output_error.py
@ Time       ：2024/9/14 1:31
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
from .base_exception import LuaDocGeneratorError

class OutputError(LuaDocGeneratorError):
    """输出错误，用于文件写入或格式转换过程中的问题"""
    pass