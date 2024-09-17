# Lua Documentation Generator 项目结构

## 目录结构

```
lua-doc-generator/
│
├── src/
│   ├── __init__.py
│   ├── main.py                 # 主程序入口
│   ├── config_utils.py         # 配置文件处理工具
│   ├── lua_parser/
│   │   ├── __init__.py
│   │   ├── parser.py           # Lua 代码解析器
│   │   └── type_analyzer.py    # 类型分析工具
│   ├── doc_generator/
│   │   ├── __init__.py
│   │   ├── generator.py        # 文档生成核心逻辑
│   │   ├── markdown_writer.py  # Markdown 格式输出
│   │   ├── html_writer.py      # HTML 格式输出
│   │   └── pdf_writer.py       # PDF 格式输出
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_utils.py       # 文件操作工具
│   │   └── string_utils.py     # 字符串处理工具
│   └── exceptions/             # 自定义异常类
│       ├── __init__.py
│       ├── base_exception.py   # 基础异常类
│       ├── config_error.py     # 配置相关错误
│       ├── parsing_error.py    # 解析相关错误
│       ├── generation_error.py # 文档生成相关错误
│       ├── template_error.py   # 模板相关错误
│       └── output_error.py     # 输出相关错误
│
├── tests/
│   ├── __init__.py
│   ├── test_config_utils.py
│   ├── test_lua_parser.py
│   ├── test_doc_generator.py
│   ├── test_utils.py
│   └── test_exceptions.py      # 测试自定义异常
│
├── templates/
│   ├── default_template.md.j2  # 默认 Markdown 模板
│   └── default_template.html.j2 # 默认 HTML 模板
│
├── docs/
│   ├── user_guide.md           # 用户指南
│   └── developer_guide.md      # 开发者指南
│
├── examples/
│   ├── simple_project/         # 简单项目示例
│   └── complex_project/        # 复杂项目示例
│
├── scripts/
│   └── install_dependencies.sh # 安装依赖脚本
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── config.yaml.example         # 示例配置文件
```

## 目录说明

### src/
包含项目的主要源代码。

- `main.py`: 程序的入口点，处理命令行参数并协调整个文档生成过程。
- `config_utils.py`: 处理配置文件的加载和解析。
- `lua_parser/`: 负责解析 Lua 代码和提取文档注释。
- `doc_generator/`: 包含将解析后的信息转换为各种输出格式的模块。
- `utils/`: 通用工具函数和类。
- `src/exceptions/`: 新增的目录，包含所有自定义异常类。

custom_exceptions.py: 定义了项目中使用的所有自定义异常类。

### tests/
包含所有的单元测试和集成测试，确保代码的正确性和稳定性。

### templates/
存储用于生成文档的 Jinja2 模板文件，允许自定义文档输出格式。

### docs/
项目自身的文档，包括用户指南和开发者指南。

### examples/
示例 Lua 项目，用于演示和测试文档生成器的功能。

### scripts/
包含各种实用脚本，如依赖安装脚本，简化项目设置和管理。

## 核心组件

1. **Lua 解析器** (`lua_parser/parser.py`): 负责解析 Lua 源代码，提取函数、类和模块信息。

2. **文档生成器** (`doc_generator/generator.py`): 将解析后的信息转换为结构化文档。

3. **输出格式处理器** (`doc_generator/*.py`): 处理不同的输出格式（Markdown、HTML、PDF）。

4. **配置管理** (`config_utils.py`): 处理用户配置，允许自定义文档生成过程。

5. **工具函数** (`utils/*.py`): 提供各种辅助功能，如文件操作和字符串处理。

6. **异常处理** (`exceptions/custom_exceptions.py`): 定义了项目特定的异常类，用于更精确的错误处理和报告。