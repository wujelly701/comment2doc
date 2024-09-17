# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : test_html_writer.py
@ Time       ：2024/9/12 1:58
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import pytest
from ..src.doc_generator.html_writer import HTMLWriter

@pytest.fixture
def writer():
    return HTMLWriter()

def test_highlight_code(writer):
    code = "function test() return 'Hello' end"
    highlighted = writer.highlight_code(code)
    assert '<span class="kr">function</span>' in highlighted
    assert '<span class="nf">test</span>' in highlighted
    assert '<span class="s1">&#39;Hello&#39;</span>' in highlighted
    assert '<span class="kr">end</span>' in highlighted

def test_write(writer, tmp_path):
    content = "<html><body>Test HTML</body></html>"
    output_file = tmp_path / "test.html"
    writer.write(content, str(output_file))
    assert output_file.read_text() == content