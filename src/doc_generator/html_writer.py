# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : html_writer.py
@ Time       ：2024/9/12 1:34
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
# html_writer.py

from pygments import highlight
from pygments.lexers import LuaLexer
from pygments.formatters import HtmlFormatter


class HTMLWriter:
    default_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project_name }} Documentation</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            height: 100vh;
            color: #333;
            transition: background-color 0.3s, color 0.3s;
        }
        body.dark-mode {
            background-color: #1a1a1a;
            color: #f0f0f0;
        }
        .sidebar {
            width: 280px;
            background-color: #f7f7f8;
            padding: 20px;
            overflow-y: auto;
            height: 100vh;
            position: fixed;
            box-shadow: 2px 0 5px rgba(0,0,0,0.1);
            transition: background-color 0.3s;
        }
        .dark-mode .sidebar {
            background-color: #2c2c2c;
            box-shadow: 2px 0 5px rgba(255,255,255,0.1);
        }
        .main-content {
            margin-left: 320px;
            padding: 40px;
            flex-grow: 1;
            overflow-y: auto;
            background-color: #fff;
            transition: background-color 0.3s;
        }
        .dark-mode .main-content {
            background-color: #333;
        }
        .search-container {
            position: relative;
            margin-bottom: 20px;
        }
        .search-icon {
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            color: #888;
        }
        .clear-icon {
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            color: #888;
            cursor: pointer;
            display: none;
        }
        .search-box {
            width: 100%;
            padding: 10px 30px 10px 35px;
            box-sizing: border-box;
            border: 1px solid #ddd;
            border-radius: 4px;
            transition: background-color 0.3s, border-color 0.3s;
        }
        .dark-mode .search-box {
            background-color: #444;
            border-color: #555;
            color: #f0f0f0;
        }
        .nav-item {
            cursor: pointer;
            padding: 8px 0;
            color: #2c3e50;
            transition: color 0.3s;
        }
        .dark-mode .nav-item {
            color: #b0b0b0;
        }
        .nav-item:hover {
            color: #3498db;
        }
        .nav-item > span {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .nav-item > span::after {
            content: '▼';
            font-size: 0.8em;
            transition: transform 0.3s;
        }
        .nav-item.collapsed > span::after {
            transform: rotate(-90deg);
        }
        .sub-nav {
            padding-left: 20px;
            overflow: hidden;
            max-height: 1000px;
            transition: max-height 0.3s ease-out;
        }
        .nav-item.collapsed .sub-nav {
            max-height: 0;
        }
        .sub-nav a {
            color: #34495e;
            text-decoration: none;
            display: block;
            padding: 5px 0;
            transition: color 0.3s;
        }
        .dark-mode .sub-nav a {
            color: #a0a0a0;
        }
        .sub-nav a:hover {
            color: #3498db;
        }
        .content-section {
            display: none;  /* 初始隐藏所有内容 */
        }
        #introduction {
            display: block;  /* 显示简介 */
        }
        .dark-mode .content-section {
            background-color: #2c2c2c;
            box-shadow: 0 1px 3px rgba(255,255,255,0.12), 0 1px 2px rgba(255,255,255,0.24);
        }
        .document-title {
            font-size: 2.5em;
            color: #2c3e50;
            margin-bottom: 30px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
        }
        .dark-mode .document-title {
            color: #ecf0f1;
            border-bottom-color: #2980b9;
        }
        h1, h2, h3, h4 {
            color: #2c3e50;
            transition: color 0.3s;
        }
        .dark-mode h1, .dark-mode h2, .dark-mode h3, .dark-mode h4 {
            color: #e0e0e0;
        }
        pre {
            background-color: #f8f8f8;
            border: 1px solid #e1e1e8;
            border-radius: 3px;
            padding: 10px;
            overflow-x: auto;
            transition: background-color 0.3s, border-color 0.3s;
        }
        .dark-mode pre {
            background-color: #2c2c2c;
            border-color: #444;
        }
        code {
            font-family: Consolas, Monaco, 'Andale Mono', monospace;
            font-size: 0.9em;
        }
        .function, .table {
            margin-bottom: 30px;
            border-left: 3px solid #3498db;
            padding-left: 15px;
            transition: border-color 0.3s;
        }
        .dark-mode .function, .dark-mode .table {
            border-left-color: #2980b9;
        }
        .highlight {
            background-color: #fff3cd;
            transition: background-color 0.5s ease;
        }
        .dark-mode .highlight {
            background-color: #4a4a00;
        }
        #mode-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 10px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .dark-mode #mode-toggle {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="sidebar">
        <h1>{{ project_name }} Documentation</h1>
        <div class="search-container">
            <span class="search-icon">🔍</span>
            <input type="text" id="search-input" class="search-box" placeholder="搜索...">
            <span class="clear-icon" id="clear-search">✖</span>
        </div>
        <div id="nav-list">
            {% for module_name, module_info in modules.items() %}
            <div class="nav-item">
                <span onclick="toggleSubNav(this.parentElement); loadContent('{{ module_name | create_anchor }}')">{{ module_name }}</span>
                <div class="sub-nav">
                    {% for func in module_info.content.functions %}
                    <a href="#{{ module_name }}.{{ func.name | create_anchor }}" onclick="loadContent('{{ module_name | create_anchor }}')">{{ func.name }}</a>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    <div class="main-content">
        <h1 class="document-title">{{ project_name }} Documentation</h1>
        
        <div id="introduction" class="content-section">
            <h2>简介</h2>
            <p>这里是{{ project_name }}项目的文档。请从左侧导航栏选择模块以查看详细信息。</p>
        </div>

        {% for module_name, module_info in modules.items() %}
        <div id="{{ module_name | create_anchor }}" class="content-section">
            <h2>Module: {{ module_name }}</h2>
            {% if module_info.module and module_info.module.description %}
                {{ module_info.module.description | markdown }}
            {% endif %}

            {% if config.include_tables and module_info.content.tables %}
            <h3>Tables</h3>
            {% for table in module_info.content.tables %}
            <div class="table" id="{{ module_name }}.{{ table.name | create_anchor }}">
                <h4>{{ table.name }}</h4>
                {% if table.is_local %}(Local table){% endif %}
                <p>{{ table.description | markdown }}</p>
                {% if table.fields %}
                <h5>Fields:</h5>
                <ul>
                {% for field in table.fields %}
                <li><strong>{{ field.name }}</strong>: {% if field.type %}<a href="#{{ field.type.name | create_anchor }}">{{ field.type }}</a>{% endif %} - {{ field.description }}</li>
                {% endfor %}
                </ul>
                {% endif %}
            </div>
            {% endfor %}
            {% endif %}

            <h3>Functions</h3>
            {% for func in module_info.content.functions %}
            {% if config.include_local_functions or not func.is_local %}
            <div class="function" id="{{ module_name }}.{{ func.name | create_anchor }}">
                <h4>{{ func.name }}</h4>
                {% if func.is_local %}(Local function){% endif %}
                <p>{{ func.description | markdown }}</p>

                {% if config.include_params and func.params %}
                <h5>Parameters:</h5>
                <ul>
                {% for param in func.params %}
                <li><strong>{{ param.name }}</strong>: {% if param.type %}<a href="#{{ param.type.name | create_anchor }}">{{ param.type }}</a>{% endif %} - {{ param.description }}</li>
                {% endfor %}
                </ul>
                {% endif %}

                {% if config.include_returns and func.returns %}
                <h5>Returns:</h5>
                <ul>
                {% for ret in func.returns %}
                <li>{% if ret.type %}<a href="#{{ ret.type.name | create_anchor }}">{{ ret.type }}</a>{% endif %} - {{ ret.description }}</li>
                {% endfor %}
                </ul>
                {% endif %}

                {% if config.include_usage and func.usage %}
                <h5>Usage:</h5>
                {{ highlight_code(func.usage, 'lua') }}
                {% endif %}

                {% if config.include_examples and func.examples %}
                <h5>Examples:</h5>
                {{ highlight_code(func.examples, 'lua') }}
                {% endif %}

                {% if config.include_see_also and func.see %}
                <h5>See also:</h5>
                <ul>
                {% for see in func.see %}
                <li><a href="#{{ see | create_anchor }}">{{ see }}</a></li>
                {% endfor %}
                </ul>
                {% endif %}
            </div>
            {% endif %}
            {% endfor %}
        </div>
        {% endfor %}
    </div>

    <button id="mode-toggle">切换夜间模式</button>

    <script>
        const searchInput = document.getElementById('search-input');
        const navList = document.getElementById('nav-list');
        const modeToggle = document.getElementById('mode-toggle');
        const body = document.body;
        const clearSearch = document.getElementById('clear-search');

        function toggleSubNav(element) {
            element.classList.toggle('collapsed');
        }

        function loadContent(moduleId) {
            // 隐藏所有内容
            document.querySelectorAll('.content-section').forEach(section => {
                section.style.display = 'none';
            });

            // 显示选中的模块内容
            const selectedModule = document.getElementById(moduleId);
            if (selectedModule) {
                selectedModule.style.display = 'block';
            }
        }

        function performSearch() {
            const searchTerm = searchInput.value.toLowerCase().trim();
            const navItems = navList.getElementsByClassName('nav-item');

            clearSearch.style.display = searchTerm ? 'block' : 'none';

            for (let item of navItems) {
                const itemText = item.textContent.toLowerCase();
                const subNav = item.querySelector('.sub-nav');
                const subItems = subNav.getElementsByTagName('a');

                let showItem = itemText.includes(searchTerm);

                for (let subItem of subItems) {
                    if (subItem.textContent.toLowerCase().includes(searchTerm)) {
                        showItem = true;
                        subItem.style.display = 'block';
                    } else {
                        subItem.style.display = 'none';
                    }
                }

                item.style.display = showItem ? 'block' : 'none';
                if (showItem) {
                    item.classList.remove('collapsed');
                }
            }
        }

        searchInput.addEventListener('input', performSearch);

        clearSearch.addEventListener('click', function() {
            searchInput.value = '';
            performSearch();
        });

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    highlightElement(targetElement);
                }
            });
        });

        function highlightElement(element) {
            element.classList.add('highlight');
            setTimeout(() => {
                element.classList.remove('highlight');
            }, 2000);
        }

        modeToggle.addEventListener('click', function() {
            body.classList.toggle('dark-mode');
            if (body.classList.contains('dark-mode')) {
                modeToggle.textContent = '切换日间模式';
            } else {
                modeToggle.textContent = '切换夜间模式';
            }
        });

        // 初始化：隐藏所有模块内容，只显示简介
        document.querySelectorAll('.content-section').forEach(section => {
            section.style.display = 'none';
        });
        document.getElementById('introduction').style.display = 'block';
    </script>
</body>
</html>
    """

    def __init__(self):
        self.lexer = LuaLexer()
        self.formatter = HtmlFormatter(cssclass='codehilite')

    def write(self, content, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

    def highlight_code(self, code, language='lua', formatter_options=None):
        if formatter_options is None:
            formatter_options = {}
        formatter = HtmlFormatter(cssclass='codehilite', **formatter_options)
        return highlight(code, self.lexer, formatter)