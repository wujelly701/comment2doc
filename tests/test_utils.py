# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : test_utils.py
@ Time       ：2024/9/12 1:59
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import pytest
from ..src.utils.file_utils import ensure_dir, get_file_content, get_relative_path
from ..src.utils.string_utils import camel_to_snake, snake_to_camel, create_anchor

def test_ensure_dir(tmp_path):
    test_dir = tmp_path / "test_directory"
    ensure_dir(str(test_dir))
    assert test_dir.exists()

def test_get_file_content(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content")
    content = get_file_content(str(test_file))
    assert content == "test content"

def test_get_relative_path(tmp_path):
    base_path = tmp_path / "project"
    file_path = base_path / "src" / "module" / "file.lua"
    relative_path = get_relative_path(str(file_path), str(base_path))
    assert relative_path == "src/module/file.lua"

def test_camel_to_snake():
    assert camel_to_snake('camelCase') == 'camel_case'
    assert camel_to_snake('ThisIsATest') == 'this_is_a_test'

def test_snake_to_camel():
    assert snake_to_camel('snake_case') == 'SnakeCase'
    assert snake_to_camel('this_is_a_test') == 'ThisIsATest'

def test_create_anchor():
    assert create_anchor('This is a test') == 'this-is-a-test'
    assert create_anchor('function_name()') == 'function_name'