# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : markdown_writer.py
@ Time       ：2024/9/12 1:34
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
from pygments import highlight
from pygments.lexers import LuaLexer
from pygments.formatters import HtmlFormatter

class MarkdownWriter:
    default_template = """
# {{ project_name }} Documentation

Version: {{ version }}

{% for file_path, file_info in modules.items() %}
## Module: {{ file_info.module.name or file_path }}

{{ file_info.module.description }}

{% if config.include_tables and file_info.content.tables %}
### Tables

{% for table in file_info.content.tables %}
#### {{ table.name }}

{% if table.is_local %}(Local table){% endif %}

{{ table.description }}

{% if table.fields %}
Fields:
{% for field in table.fields %}
- **{{ field.name }}**: {% if field.type %}[{{ field.type }}](#{{ field.type.name | create_anchor }}){% endif %} - {{ field.description }}
{% endfor %}
{% endif %}

{% endfor %}
{% endif %}

### Functions

{% for func in file_info.content.functions %}
{% if config.include_local_functions or not func.is_local %}
#### {{ func.name }}

{% if func.is_local %}(Local function){% endif %}

{{ func.description }}

{% if config.include_params and func.params %}
Parameters:
{% for param in func.params %}
- **{{ param.name }}**: {% if param.type %}[{{ param.type }}](#{{ param.type.name | create_anchor }}){% endif %} - {{ param.description }}
{% endfor %}
{% endif %}

{% if config.include_returns and func.returns %}
Returns:
{% for ret in func.returns %}
- {% if ret.type %}[{{ ret.type }}](#{{ ret.type.name | create_anchor }}){% endif %} - {{ ret.description }}
{% endfor %}
{% endif %}

{% if config.include_usage and func.usage %}
Usage:
```lua
{{ func.usage }}
```
{% endif %}

{% if config.include_examples and func.examples %}
Examples:
```lua
{{ func.examples }}
```
{% endif %}
{% if config.include_see_also and func.see %}
See also:
{% for see in func.see %}

[{{ see }}](#{{ see | create_anchor }})
{% endfor %}
{% endif %}

{% endif %}
{% endfor %}
{% endfor %}
{% if config.include_type_index %}
Type Index
{% for type_name, occurrences in type_index.items() %}
{{ type_name }}
Used in:
{% for occurrence in occurrences %}

[{{ occurrence.module }}](#{{ occurrence.module | create_anchor }}): {{ occurrence.context }}
{% endfor %}

{% endfor %}
{% endif %}
Function Index
{% for func_name, func_info in function_index.items() %}

[{{ func_name }}](#{{ (func_info.module + '.' + func_info.name) | create_anchor }})
{% endfor %}

Table Index
{% for table_name, table_info in table_index.items() %}

[{{ table_name }}](#{{ (table_info.module + '.' + table_info.name) | create_anchor }})
{% endfor %}
"""

    def write(self, content, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

    def highlight_code(self, code, language='lua', formatter_options=None):
        if formatter_options is None:
            formatter_options = {}
        return f'\n```{language}\n{code}\n```\n'