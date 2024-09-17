# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : generator.py.py
@ Time       ：2024/9/12 1:33
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import os
import re
from jinja2 import Environment, FileSystemLoader
import markdown
from .markdown_writer import MarkdownWriter
from .html_writer import HTMLWriter
from .pdf_writer import PDFWriter

def basename_filter(path):
    return os.path.basename(path)

def markdown_filter(text):
    return markdown.markdown(text, extensions=['fenced_code', 'codehilite'])

def create_anchor_filter(text):
    return re.sub(r'[^\w\- ]', '', text.lower().replace(' ', '-'))

class DocGenerator:
    def __init__(self, config, verbose=False):
        self.config = config
        self.verbose = verbose
        self.writers = {
            'md': MarkdownWriter(),
            'markdown': MarkdownWriter(),
            'html': HTMLWriter(),
            'pdf': PDFWriter()
        }
        self.jinja_env = Environment(loader=FileSystemLoader('.'))
        self.jinja_env.filters['basename'] = basename_filter
        self.jinja_env.filters['markdown'] = markdown_filter
        self.jinja_env.filters['create_anchor'] = create_anchor_filter

    def generate(self, parsed_data, output_file, template_path=None):
        output_format = os.path.splitext(output_file)[1][1:]  # Get format from file extension
        if output_format == '':
            output_format = 'md'  # Default to markdown if no extension is provided

        writer = self.writers.get(output_format.lower())
        if not writer:
            raise ValueError(f"Unsupported output format: {output_format}")

        if template_path:
            with open(template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
        else:
            template_content = writer.default_template

        template = self.jinja_env.from_string(template_content)
        content = template.render(
            project_name=self.config['project_name'],
            version=self._get_version(),
            modules=parsed_data,
            config=self.config,
            type_index=self._build_type_index(parsed_data),
            function_index=self._build_function_index(parsed_data),
            table_index=self._build_table_index(parsed_data),
            highlight_code=writer.highlight_code
        )

        writer.write(content, output_file)

        if self.verbose:
            print(f"Documentation generated successfully in {output_file}")

    def generate_coverage_report(self, parsed_data):
        total_functions = 0
        documented_functions = 0
        total_tables = 0
        documented_tables = 0

        for file_data in parsed_data.values():
            total_functions += len(file_data['content']['functions'])
            documented_functions += sum(1 for func in file_data['content']['functions'] if func['description'])
            total_tables += len(file_data['content']['tables'])
            documented_tables += sum(1 for table in file_data['content']['tables'] if table['description'])

        function_coverage = (documented_functions / total_functions) * 100 if total_functions else 0
        table_coverage = (documented_tables / total_tables) * 100 if total_tables else 0

        report = f"""
        Documentation Coverage Report:
        ------------------------------
        Functions: {documented_functions}/{total_functions} ({function_coverage:.2f}%)
        Tables: {documented_tables}/{total_tables} ({table_coverage:.2f}%)
        """
        return report

    def _get_version(self):
        if self.config.get('version'):
            return self.config['version']
        elif self.config.get('use_git_version'):
            import subprocess
            try:
                return subprocess.check_output(['git', 'describe', '--tags', '--always']).strip().decode()
            except subprocess.CalledProcessError:
                if self.verbose:
                    print("Warning: Unable to get git version, using default version")
                return "0.1.0"
        else:
            return "0.1.0"

    def _build_type_index(self, parsed_data):
        type_index = {}
        for file_path, file_data in parsed_data.items():
            module_name = os.path.splitext(os.path.basename(file_path))[0]
            for func in file_data['content']['functions']:
                for param in func.get('params', []):
                    if param.get('type'):
                        self._add_to_type_index(type_index, param['type'], module_name, f"{func['name']} (parameter)")
                for ret in func.get('returns', []):
                    if ret.get('type'):
                        self._add_to_type_index(type_index, ret['type'], module_name, f"{func['name']} (return)")
            for table in file_data['content']['tables']:
                for field in table.get('fields', []):
                    if field.get('type'):
                        self._add_to_type_index(type_index, field['type'], module_name, f"{table['name']}.{field['name']}")
        return type_index

    def _add_to_type_index(self, type_index, lua_type, module_name, context):
        if lua_type.name not in type_index:
            type_index[lua_type.name] = []
        type_index[lua_type.name].append({'module': module_name, 'context': context})
        for subtype in lua_type.subtypes:
            self._add_to_type_index(type_index, subtype, module_name, context)

    def _build_function_index(self, parsed_data):
        function_index = {}
        for file_path, file_data in parsed_data.items():
            module_name = os.path.splitext(os.path.basename(file_path))[0]
            for func in file_data['content']['functions']:
                function_index[f"{module_name}.{func['name']}"] = {
                    'module': module_name,
                    'name': func['name'],
                    'params': func['params'],
                    'returns': func['returns']
                }
        return function_index

    def _build_table_index(self, parsed_data):
        table_index = {}
        for file_path, file_data in parsed_data.items():
            module_name = os.path.splitext(os.path.basename(file_path))[0]
            for table in file_data['content']['tables']:
                table_index[f"{module_name}.{table['name']}"] = {
                    'module': module_name,
                    'name': table['name'],
                    'fields': table['fields']
                }
        return table_index