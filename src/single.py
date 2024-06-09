# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : single.py
@ Time       ：2024/6/9 13:21
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import os
import re
from datetime import datetime


def run(file1, file2):
    print('doing ' + file1)

    file_path = file1
    out_file = file2

    if not file_path:
        print('未设置文件路径')
        return

    # 转为绝对路径
    file_path = os.path.abspath(file_path)

    file_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path)

    # 设置输出路径
    if not out_file:
        out_file = os.path.dirname(file_path)
        out_file = os.path.abspath(out_file)

    print('输出目录',file_path)
    out_dir = file_path[len(os.path.dirname(__file__)) + len('test/'):]
    print('输出目录',out_dir)
    out_dir = os.path.join(os.path.dirname(__file__), 'out', out_dir)
    print('输出目录',out_dir)
    # 判断目录是否存在
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    out_file = os.path.join(out_dir, file_name + '.md')

    apis = []

    api = {
        'brief': '',
        'params': [],
        'return': None,
    }

    content = ''

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    docs = []
    one = []
    start = False
    last = False
    for line in lines:
        line = line.strip()
        if line == '-- /**':  # 开始
            one = []
            start = True
            one.append(line)
        elif line == '--  */':  # 结束
            if start:
                start = False
                one.append(line)
                last = True
        else:
            if start:
                one.append(line)
            if last:  # 函数声明行
                last = False
                one.append(line)
                docs.append(one)

    for one in docs:
        parser_api(one, apis)

    content += f'修改日期: {str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}\n\r'
    content += '### 0. 索引\n\r'
    for i, api in enumerate(apis):
        content += f'[{i+1}. {api["name"]}](#{i+1})\n\n'
    content += '\n\r'
    content += '---\n\r'

    for i, api in enumerate(apis):
        content = append_content(api, i + 1, content)

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(content)


BRIEF_FORMAT = '--  *'
PARAM_FORMAT = '--  * @param'
RETURN_FORMAT = '--  * @return'

TYPE_REG = r'^\{.*?\}'

def parser_param(param):
    detail = param[len(PARAM_FORMAT):].strip()
    # 类型
    type_match = re.search(TYPE_REG, detail)
    if not type_match:
        return

    # 字段
    p2 = detail[len(type_match.group()):].strip().split(' ', 1)
    field = p2[0]  # 不能带空格
    explain = p2[1]  # 不能带空格

    remark = ' '.join(p2[2:])  # 防止备注中有空格

    type_str = type_match.group()[1:-1]
    can_null = False
    if 'null' not in type_str:
        type_str = type_str.replace('*', 'any')
    else:
        can_null = True
        s = type_str.find('|')
        if s > 0:
            type_str = type_str[:s].strip()

    return {
        'type': type_str,
        'canNull': can_null,
        'field': field,
        'explain': explain,
        'remark': remark,
    }

def parser_api(lines, apis):
    api = {
        'name': '',
        'brief': '',
        'params': [],
        'return': None,
    }

    for line in lines[:-2]:
        if line.startswith(PARAM_FORMAT):
            param = parser_param(line)
            if param:
                api['params'].append(param)
        elif line.startswith(RETURN_FORMAT):
            result = line[len(RETURN_FORMAT):].strip()
            # 类型
            type_match = re.search(TYPE_REG, result)
            if type_match:
                api['return'] = {
                    'type': type_match.group()[1:-1],
                    'explain': result[len(type_match.group()):].strip(),
                }
        elif line.startswith(BRIEF_FORMAT):
            api['brief'] = line[len(BRIEF_FORMAT):].strip()

    # 获取函数名字
    last_line = lines[-1]
    name_match = re.search(r':(.*)\(', last_line)
    if name_match:
        api['name'] = name_match.group(1)
    else:
        name_match = re.search(r'\.(.*)\(', last_line)
        api['name'] = name_match.group(1)

    apis.append(api)

def append_content(api, idx, content):
    content += f'<h3><span id={idx}>{idx}. {api["name"]}</span></h3>\n\r'
    content += '__简要描述__\n\r'
    content += '- ' + api['brief'] + '\n\r'
    content += '__参数__\n\r'
    if not api['params']:
        content += '- 无参数\n\r'
    else:
        content += '|参数名|类型|必选|说明|备注|\n'
        content += '|:--|:--|:--|:--|:--|\n'
        for param in api['params']:
            content += f'|{param["field"]}|{param["type"]}|{"否" if param["canNull"] else "是"}|{param["explain"]}|{param["remark"]}|\n'
    content += '\n\r'
    content += '__返回值说明__\n\r'
    if api['return']:
        content += '|类型|说明|\n'
        content += '|:--|:--|\n'
        content += f'|{api["return"]["type"]}|{api["return"]["explain"]}|\n\r'
    else:
        content += '- 无返回值\n\r'
    content += '---\n'
    return content
