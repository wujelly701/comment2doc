# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : setup.py
@ Time       ：2024/9/12 2:02
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lua-doc-generator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A documentation generator for Lua projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/lua-doc-generator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "PyYAML>=5.4.1",
        "Jinja2>=2.11.3",
        "Pygments>=2.9.0",
        "Markdown>=3.3.4",
        "pdfkit>=0.6.1",
    ],
    entry_points={
        "console_scripts": [
            "lua-doc-generator=lua_doc_generator.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "lua_doc_generator": ["templates/*.md.j2", "templates/*.html.j2"],
    },
)