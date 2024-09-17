# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : file_utils.py
@ Time       ：2024/9/12 1:36
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import os

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_relative_path(file_path, base_path):
    rel_path = os.path.relpath(file_path, base_path)
    # 将反斜杠替换为正斜杠
    return rel_path.replace(os.sep, '/')