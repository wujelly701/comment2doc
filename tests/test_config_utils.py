# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : test_config_utils.py
@ Time       ：2024/9/12 1:56
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import tempfile
import os
from ..src.config_utils import load_config


def test_load_config_default():
    config = load_config(None)
    assert config['project_name'] == 'Lua Project'
    assert config['file_extensions'] == ['.lua']
    assert config['include_params'] == True


def test_load_config_custom():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
        temp.write("""
        project_name: Custom Project
        file_extensions:
          - .lua
          - .luau
        include_params: false
        """)

    config = load_config(temp.name)
    os.unlink(temp.name)

    assert config['project_name'] == 'Custom Project'
    assert config['file_extensions'] == ['.lua', '.luau']
    assert config['include_params'] == False