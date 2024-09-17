# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : type_analyzer.py.py
@ Time       ：2024/9/12 1:32
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import re

class LuaType:
    def __init__(self, type_str):
        self.original = type_str
        self.name, self.subtypes = self._parse_type(type_str)

    def __str__(self):
        if not self.subtypes:
            return self.name
        return f"{self.name}<{', '.join(str(t) for t in self.subtypes)}>"

    def _parse_type(self, type_str):
        match = re.match(r'(\w+)(?:<(.+)>)?', type_str)
        if not match:
            return type_str, []
        name, subtypes_str = match.groups()
        if subtypes_str:
            return name, [LuaType(t.strip()) for t in subtypes_str.split(',')]
        return name, []

    def to_dict(self):
        return {
            'name': self.name,
            'subtypes': [t.to_dict() for t in self.subtypes],
            'original': self.original
        }