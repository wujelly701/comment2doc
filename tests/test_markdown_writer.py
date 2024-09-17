# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : test_markdown_writer.py
@ Time       ：2024/9/12 1:58
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import pytest
from src.doc_generator.markdown_writer import MarkdownWriter
from src.doc_generator.html_writer import HTMLWriter


@pytest.fixture
def markdown_writer():
    return MarkdownWriter()


@pytest.fixture
def html_writer():
    return HTMLWriter()


def test_highlight_code_markdown(markdown_writer):
    code = "function test() return 'Hello' end"
    highlighted = markdown_writer.highlight_code(code)

    assert highlighted.strip() == "```lua\nfunction test() return 'Hello' end\n```"


def test_highlight_code_html(html_writer):
    code = "function test() return 'Hello' end"
    highlighted = html_writer.highlight_code(code)

    assert '<span class="kr">function</span>' in highlighted
    assert '<span class="nf">test</span>' in highlighted
    assert '<span class="s1">&#39;Hello&#39;</span>' in highlighted
    assert '<span class="kr">end</span>' in highlighted
    assert '<div class="codehilite">' in highlighted