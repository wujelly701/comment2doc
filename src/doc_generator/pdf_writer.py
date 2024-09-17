# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : pdf_writer.py
@ Time       ：2024/9/12 1:35
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import pdfkit
from .html_writer import HTMLWriter
import sys
import os


class PDFWriter(HTMLWriter):
    def __init__(self):
        super().__init__()
        self.default_template = self.default_template  # Reuse HTML template

    def write(self, content, output_file):
        options = {
            'encoding': 'UTF-8',
            'no-outline': None,
            'quiet': '',
        }

        # 尝试找到 wkhtmltopdf 的路径
        wkhtmltopdf_path = self.find_wkhtmltopdf()

        try:
            if wkhtmltopdf_path:
                config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
                pdfkit.from_string(content, output_file, options=options, configuration=config)
            else:
                pdfkit.from_string(content, output_file, options=options)
        except Exception as e:
            error_message = f"Error generating PDF: {str(e)}"
            print(error_message, file=sys.stderr)
            raise IOError(error_message)

    def highlight_code(self, code, language='lua', formatter_options=None):
        # 重用 HTMLWriter 的代码高亮方法
        return super().highlight_code(code, language, formatter_options)

    def find_wkhtmltopdf(self):
        # 常见的安装路径
        common_paths = [
            r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
            '/usr/local/bin/wkhtmltopdf',
            '/usr/bin/wkhtmltopdf',
            r'D:\program\wkhtmltox\bin\wkhtmltopdf.exe',
        ]

        # 检查常见路径
        for path in common_paths:
            if os.path.isfile(path):
                return path

        # 检查系统 PATH
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, 'wkhtmltopdf')
            if os.path.isfile(exe_file):
                return exe_file

        return None
