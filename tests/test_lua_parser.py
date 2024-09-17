# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : test_lua_parser.py
@ Time       ：2024/9/12 1:57
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import pytest
from unittest.mock import patch
from src.lua_parser.parser import LuaParser
from src.lua_parser.type_analyzer import LuaType


@pytest.fixture
def parser():
    return LuaParser({'file_extensions': ['.lua']})


@pytest.fixture
def parser():
    config = {
        'file_extensions': ['.lua']
    }
    return LuaParser(config)


@patch('chardet.detect')
def test_parse_function(mock_detect, parser, tmp_path):
    mock_detect.return_value = {'encoding': 'utf-8'}

    lua_code = """
    ---This is a test function
    ---It demonstrates basic functionality
    ---@param name string The name to greet
    ---@return string The greeting message
    function greet(name)
        return "Hello, " .. name
    end
    """

    # 创建一个临时文件
    test_file = tmp_path / "test.lua"
    test_file.write_text(lua_code, encoding='utf-8')

    # 调用 parse_file 方法
    parsed_data = parser.parse_file(str(test_file))

    functions = parsed_data['functions']

    assert len(functions) == 1
    assert functions[0]['name'] == 'greet'
    assert functions[0]['description'] == 'This is a test function\nIt demonstrates basic functionality'
    assert len(functions[0]['params']) == 1
    assert functions[0]['params'][0]['name'] == 'name'
    assert isinstance(functions[0]['params'][0]['type'], LuaType)
    print(functions)
    assert str(functions[0]['params'][0]['type']) == 'string'
    assert functions[0]['params'][0]['description'] == 'The name to greet'
    assert len(functions[0]['returns']) == 1
    assert isinstance(functions[0]['returns'][0]['type'], LuaType)
    assert str(functions[0]['returns'][0]['type']) == 'string'
    assert functions[0]['returns'][0]['description'] == 'The greeting message'
    assert functions[0]['is_local'] == False
    assert 'line_number' in functions[0]

    # 打印实际的函数信息，以便调试
    print("Actual function info:", functions[0])

@patch('chardet.detect')
def test_parse_table(mock_detect, parser, tmp_path):
    mock_detect.return_value = {'encoding': 'utf-8'}
    lua_code = """
    ---@class Person
    ---@field name string The person's name
    ---@field age number The person's age
    local Person = {
        name = "",
        age = 0
    }
    """
    # 创建一个临时文件
    test_file = tmp_path / "test.lua"
    test_file.write_text(lua_code, encoding='utf-8')

    parsed_data = parser.parse_file(str(test_file))

    tables = parsed_data['tables']

    print(tables)

    assert len(tables) == 1
    assert tables[0]['name'] == 'Person'
    assert len(tables[0]['fields']) == 2
    assert tables[0]['fields'][0]['name'] == 'name'
    assert isinstance(tables[0]['fields'][0]['type'], LuaType)
    assert str(tables[0]['fields'][0]['type']) == 'string'
