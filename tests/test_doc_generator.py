# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : test_doc_generator.py
@ Time       ：2024/9/12 1:58
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import pytest
from ..src.doc_generator.generator import DocGenerator
from ..src.lua_parser.type_analyzer import LuaType

@pytest.fixture
def doc_generator():
    config = {
        'project_name': 'Test Project',
        'include_params': True,
        'include_returns': True,
        'include_type_index': True
    }
    return DocGenerator(config)

def test_build_type_index(doc_generator):
    parsed_data = {
        'test.lua': {
            'functions': [
                {
                    'name': 'test_func',
                    'params': [{'name': 'param1', 'type': LuaType('string')}],
                    'returns': [{'type': LuaType('number')}]
                }
            ]
        }
    }
    type_index = doc_generator._build_type_index(parsed_data)

    assert 'string' in type_index
    assert 'number' in type_index
    assert len(type_index['string']) == 1
    assert len(type_index['number']) == 1
    assert type_index['string'][0]['context'] == 'test_func (parameter)'
    assert type_index['number'][0]['context'] == 'test_func (return)'

def test_generate_coverage_report(doc_generator):
    parsed_data = {
        'test.lua': {
            'functions': [
                {'name': 'func1', 'description': 'Documented function'},
                {'name': 'func2', 'description': ''}
            ],
            'tables': [
                {'name': 'table1', 'description': 'Documented table'},
                {'name': 'table2', 'description': ''}
            ]
        }
    }
    report = doc_generator.generate_coverage_report(parsed_data)

    assert 'Functions: 1/2 (50.00%)' in report
    assert 'Tables: 1/2 (50.00%)' in report