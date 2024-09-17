# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : generation_error.py
@ Time       ：2024/9/14 1:30
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
from .base_exception import LuaDocGeneratorError

class DocumentGenerationError(LuaDocGeneratorError):
    """文档生成错误，用于文档生成过程中的问题"""
    pass