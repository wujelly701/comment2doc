# Lua Documentation Generator 配置指南

配置文件 (`config.yaml`) 允许你自定义文档生成过程。以下是可用的配置选项：

## 基本配置

```yaml
project_name: My Lua Project
file_extensions:
  - .lua
  - .luau
output_format: markdown
```

- `project_name`: 项目名称，将显示在生成的文档中。
- `file_extensions`: 要处理的文件扩展名列表。
- `output_format`: 输出格式（markdown、html 或 pdf）。

## 文档内容控制

```yaml
include_params: true
include_returns: true
include_usage: true
include_examples: true
include_see_also: true
include_local_functions: false
include_tables: true
include_type_index: true
```

这些选项控制哪些元素会包含在生成的文档中。

## 样式和格式

```yaml
syntax_highlight: true
theme: default
code_block_style: github
```

- `syntax_highlight`: 是否启用代码语法高亮。
- `theme`: 文档主题（仅适用于 HTML 输出）。
- `code_block_style`: 代码块的样式。

## 版本控制

```yaml
use_git_version: true
version: "1.0.0"
```

- `use_git_version`: 是否使用 Git 标签作为版本号。
- `version`: 手动指定版本号（当 `use_git_version` 为 false 时使用）。

## 多文件模块

```yaml
multi_file_modules:
  - name: core
    files:
      - src/core/init.lua
      - src/core/utils.lua
  - name: ui
    files:
      - src/ui/main.lua
      - src/ui/components.lua
```

这允许你定义跨多个文件的模块。

## 高级选项

```yaml
custom_sections:
  - name: "注意事项"
    content: "这里是一些重要的注意事项..."
ignore_patterns:
  - "test_*.lua"
  - "*_spec.lua"
```

- `custom_sections`: 添加自定义部分到文档中。
- `ignore_patterns`: 指定要忽略的文件模式。

更多高级配置选项，请参阅 [高级配置指南](advanced-configuration.md)。