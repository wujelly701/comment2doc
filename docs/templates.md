# Lua Documentation Generator 模板指南

## 模板基础

Lua Documentation Generator 使用 Jinja2 模板引擎。你可以创建自定义模板来控制文档的结构和样式。

## 基本模板示例

```markdown
# {{ project_name }} Documentation

Version: {{ version }}

{% for module_name, module_info in modules.items() %}
## Module: {{ module_name }}

{{ module_info.doc }}

{% for func in module_info.functions %}
### {{ func.name }}

{{ func.description }}

{% if config.include_params and func.params %}
Parameters:
{% for param in func.params %}
- `{{ param.name }}` ({{ param.type }}): {{ param.description }}
{% endfor %}
{% endif %}

{% if config.include_returns and func.returns %}
Returns:
{% for ret in func.returns %}
- {{ ret.type }}: {{ ret.description }}
{% endfor %}
{% endif %}

{% endfor %}
{% endfor %}
```

## 可用变量

- `project_name`: 项目名称
- `version`: 文档版本
- `modules`: 模块列表，每个模块包含 `functions` 和 `tables`
- `type_index`: 类型索引
- `function_index`: 函数索引
- `table_index`: 表索引
- `config`: 配置选项

## 高级模板技巧

1. 条件渲染：

```jinja2
{% if config.include_examples and func.examples %}
Examples:
{{ func.examples | highlight_code }}
{% endif %}
```

2. 循环和过滤：

```jinja2
{% for func in module_info.functions | sort(attribute='name') %}
  {# 函数内容 #}
{% endfor %}
```

3. 宏的使用：

```jinja2
{% macro render_type(type) %}
<a href="#{{ type | create_anchor }}">{{ type }}</a>
{% endmacro %}

{{ render_type(param.type) }}
```

4. 包含其他模板：

```jinja2
{% include 'header.md.j2' %}
```

5. 继承基础模板：

```jinja2
{% extends 'base.md.j2' %}

{% block content %}
  {# 自定义内容 #}
{% endblock %}
```

## 自定义过滤器

你可以在 Python 代码中注册自定义过滤器：

```python
def highlight_code(code, language='lua'):
    # 实现代码高亮逻辑
    return highlighted_code

template.globals['highlight_code'] = highlight_code
```

然后在模板中使用：

```jinja2
{{ code_snippet | highlight_code('lua') }}
```

更多 Jinja2 模板语法和技巧，请参阅 [Jinja2 文档](https://jinja.palletsprojects.com/)。