# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : template_error.py
@ Time       ：2024/9/14 1:31
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
from .base_exception import LuaDocGeneratorError

class TemplateError(LuaDocGeneratorError):
    """模板错误，用于模板渲染过程中的问题"""
    pass