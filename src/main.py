# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : main.py
@ Time       ：2024/9/12 1:40
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import argparse
import sys
import os
import json
import traceback
from config_utils import load_config
from lua_parser.parser import LuaParser
from doc_generator.generator import DocGenerator

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录（假设 src 是项目的直接子目录）
project_root = os.path.dirname(current_dir)

# 将项目根目录和 src 目录都添加到 Python 路径
sys.path.insert(0, project_root)
sys.path.insert(0, current_dir)

def main():
    parser = argparse.ArgumentParser(description='Generate documentation for Lua projects.')
    parser.add_argument('project_path', help='Path to the Lua project')
    parser.add_argument('-o', '--output', default='lua_api_docs.md', help='Output file name')
    parser.add_argument('-c', '--config', default='config.yaml', help='Path to the configuration file')
    parser.add_argument('-t', '--template', help='Path to the custom template file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--coverage', action='store_true', help='Generate coverage report')
    args = parser.parse_args()

    config = load_config(args.config)

    lua_parser = LuaParser(config)
    doc_generator = DocGenerator(config, verbose=args.verbose)

    try:
        parsed_data = lua_parser.parse_project(args.project_path)
        if args.verbose:
            print("Parsed data structure:")
            for file_path, file_data in parsed_data.items():
                print(f"File: {file_path}")
                print(json.dumps(file_data, indent=2, default=str))
                print("-" * 50)

        print("Starting document generation...")
        doc_generator.generate(parsed_data, args.output, template_path=args.template)
        print("Document generation completed.")

        if args.coverage:
            coverage_report = doc_generator.generate_coverage_report(parsed_data)
            print(coverage_report)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        if args.verbose:
            print("Detailed error information:")
            print(traceback.format_exc())
            print("\nParsed data at the point of error:")
            print(json.dumps(parsed_data, indent=2, default=str))
        sys.exit(1)


if __name__ == "__main__":
    main()