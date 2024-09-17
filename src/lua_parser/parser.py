# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : parser.py
@ Time       ：2024/9/12 1:32
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import os
import re
import logging

from custom_exceptions.parsing_error import ParsingError
from .type_analyzer import LuaType

class LuaParser:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def parse_project(self, project_path):
        parsed_data = {}
        for root, _, files in os.walk(project_path):
            for file in files:
                if file.endswith(tuple(self.config['file_extensions'])):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, project_path)
                    file_data = self.parse_file(file_path)
                    parsed_data[relative_path] = file_data  # 直接使用 parse_file 的返回值
        return parsed_data

    def parse_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        module_doc = self._extract_module_doc(content)
        functions = self._parse_functions(content)
        tables = self._parse_tables(content)

        return {
            'module': module_doc,
            'content': {
                'functions': functions,
                'tables': tables
            }
        }

    def _extract_module_doc(self, content):
        module_pattern = r'---@module\s+(.*?)\n((?:---.*?\n)*)'
        match = re.search(module_pattern, content, re.DOTALL)
        if match:
            module_name = match.group(1).strip()
            module_description = re.sub(r'^---\s?', '', match.group(2), flags=re.MULTILINE).strip()
            return {
                'name': module_name,
                'description': module_description
            }
        return {'name': '', 'description': ''}

    def _parse_functions(self, content):
        functions = []
        pattern = r'((?:---[^\n]*\n)+)(function\s+[\w.]+\s*\([^)]*\).*?end)'
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            doc, func_body = match[0], match[1]
            function_info = self._parse_function_doc(doc)
            func_name, local = self._extract_function_info(func_body)
            function_info['name'] = func_name
            function_info['is_local'] = bool(local)
            function_info['line_number'] = self._count_function_lines(func_body)
            functions.append(function_info)

        return functions

    def _extract_function_info(self, func_body):
        # 正则表达式模式
        pattern = r'(local\s+)?function\s+([\w.:]+)\s*\('

        # 搜索匹配
        match = re.search(pattern, func_body)

        if match:
            local_modifier = match.group(1)
            function_name = match.group(2)

            is_local = bool(local_modifier)

            return function_name, is_local
        else:
            return None

    def _count_function_lines(self, func_body):
        # 使用正则表达式匹配整个函数定义
        pattern = r'function\s+[\w.]+\s*\([^)]*\)(.*?)end'
        match = re.search(pattern, func_body, re.DOTALL)

        if not match:
            return 0  # 如果没有匹配到函数，返回0

        function_body = match.group(1)
        lines = function_body.split('\n')

        # 计算非空且非纯注释的行数
        non_empty_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('--')]

        # 加上 function 声明行和 end 行
        return len(non_empty_lines) + 2

    def _parse_function_doc(self, doc):
        lines = doc.strip().split('\n')
        func_info = {
            'description': [],
            'params': [],
            'returns': [],
            'usage': [],
            'examples': [],
            'see': []
        }
        current_section = 'description'

        for line in lines:
            line = line.strip().lstrip('-').strip()  # 移除开头的破折号和空白
            if line.startswith('@param'):
                current_section = 'params'
                param_match = re.match(r'@param\s+(\w+)\s+(\S+)\s*(.*)', line)
                if param_match:
                    name, type_str, desc = param_match.groups()
                    func_info['params'].append({
                        'name': name,
                        'type': LuaType(type_str),
                        'description': desc.strip()
                    })
            elif line.startswith('@return'):
                current_section = 'returns'
                return_match = re.match(r'@return\s+(\S+)\s*(.*)', line)
                if return_match:
                    type_str, desc = return_match.groups()
                    func_info['returns'].append({
                        'type': LuaType(type_str),
                        'description': desc.strip()
                    })
            elif line.startswith('@usage'):
                current_section = 'usage'
                func_info['usage'].append(line[6:].strip())
            elif line.startswith('@example'):
                current_section = 'examples'
                func_info['examples'].append(line[8:].strip())
            elif line.startswith('@see'):
                current_section = 'see'
                func_info['see'].append(line[4:].strip())
            elif current_section == 'description' and line:  # 只有非空行才添加到描述中
                func_info['description'].append(line)
            elif current_section == 'examples' and line:
                func_info['examples'].append(line)
            elif current_section == 'see' and line:
                func_info['see'].append(line)
            elif current_section == 'usage' and line:
                func_info['usage'].append(line)

        # 处理多行内容
        func_info['description'] = '\n'.join(func_info['description']).strip()
        func_info['usage'] = '\n'.join(func_info['usage'])
        func_info['examples'] = '\n'.join(func_info['examples'])

        return func_info

    def _parse_tables(self, content):
        tables = []
        # 更新正则表达式以匹配更多表定义模式
        pattern = r'((?:---[^\n]*\n)+)(?:(local)\s+)?(\w+(?:\.\w+)*)\s*=\s*(\{[^}]*\})'
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            doc, local, table_name, table_body = match[0], match[1], match[2], match[3]
            table_info = self._parse_table_doc(doc) if doc else {}
            table_info['name'] = table_name
            table_info['is_local'] = bool(local)
            table_info['line_number'] = table_body.count('\n') + 1
            # table_info['content'] = table_content.strip()
            tables.append(table_info)

        return tables

    def _parse_table_doc(self, doc):
        """解析表文档，提取描述和字段信息"""
        lines = doc.strip().split('\n')
        table_info = {
            'description': [],
            'fields': []
        }
        current_section = 'description'

        for line in lines:
            line = line.strip().lstrip('-').strip()  # 移除开头的破折号和空白
            if line.startswith('@module'):
                continue  # 忽略 @module 标记
            try:
                if line.startswith('@field'):
                    field_match = re.match(r'@field\s+(\w+)\s+(\S+)?\s*(.*)', line)
                    if field_match:
                        name, type_str, desc = field_match.groups()
                        type_ = LuaType(type_str) if type_str else None
                        table_info['fields'].append({
                            'name': name,
                            'type': type_,
                            'description': desc
                        })
                    else:
                        raise ParsingError(f"Invalid @field format: {line}")
                else:
                    table_info['description'].append(line)
            except ParsingError as e:
                self.logger.warning(f"解析表文档行时发生错误: {str(e)}")

        # Join multi-line description
        table_info['description'] = '\n'.join(table_info['description']).strip()

        return table_info