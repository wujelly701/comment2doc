# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : config_utils.py
@ Time       ：2024/9/12 1:41
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import yaml

def load_config(config_file):
    default_config = {
        'project_name': 'Lua Project',
        'file_extensions': ['.lua'],
        'include_params': True,
        'include_returns': True,
        'include_usage': True,
        'include_examples': True,
        'include_see_also': True,
        'include_local_functions': True,
        'include_tables': True,
        'include_type_index': True,
        'syntax_highlight': True,
        'use_git_version': False,
        'version': None,
        'output_format': 'markdown',
    }

    if config_file:
        try:
            with open(config_file, 'r') as f:
                user_config = yaml.safe_load(f)
            default_config.update(user_config)
        except Exception as e:
            print(f"Error loading config file: {e}")
            print("Using default configuration.")

    return default_config