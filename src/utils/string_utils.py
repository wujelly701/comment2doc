# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : string_utils.py
@ Time       ：2024/9/12 1:36
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import re

def camel_to_snake(name):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub('_', name).lower()

def snake_to_camel(name):
    return ''.join(word.title() for word in name.split('_'))

def create_anchor(text):
    return re.sub(r'[^\w\- ]', '', text.lower().replace(' ', '-'))