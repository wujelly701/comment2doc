# comment2doc

自动为项目生成清晰、结构化的 API 文档。
目前实现
自动为 Lua 项目生成清晰、结构化的 API 文档。

## 目录

1. [谁应该使用这个工具？](#谁应该使用这个工具)
2. [特性](#特性)
3. [快速开始](#快速开始)
4. [安装](#安装)
5. [使用指南](#使用指南)
6. [配置](#配置)
7. [高级功能](#高级功能)
8. [自定义模板](#自定义模板)
9. [安全考虑](#安全考虑)
10. [故障排除与FAQ](#故障排除与faq)
11. [与其他工具的比较](#与其他工具的比较)
12. [贡献指南](#贡献指南)
13. [路线图](#路线图)
14. [许可证](#许可证)

## 谁应该使用这个工具？

- Lua 库和框架开发者
- 需要生成项目 API 文档的 Lua 开发团队
- 希望提高代码可维护性的个人开发者
- 教育工作者和学生，用于学习和教学 Lua 项目文档化

## 特性

- 多格式输出：Markdown、HTML、PDF
- 智能解析：自动识别函数、表、模块和类
- 类型注解支持
- 交叉引用和类型索引
- 自定义 Jinja2 模板
- Git 版本控制集成
- 文档覆盖率报告
- 多文件模块支持
- 代码语法高亮
- 高度可配置

## 快速开始

1. 克隆仓库并安装依赖：
   ```bash
   git clone https://github.com/your-username/lua-doc-generator.git
   cd lua-doc-generator
   pip install -r requirements.txt
   ```

2. 在 Lua 项目根目录创建 `config.yaml`：
   ```yaml
   project_name: My Lua Project
   file_extensions: [.lua]
   ```

3. 运行文档生成器：
   ```bash
   python src/main.py /path/to/your/lua/project -o docs.html
   ```

4. 查看生成的 `docs.html` 文件。
   ![image](https://github.com/user-attachments/assets/41853da1-6e06-47b6-9aaf-c154e1fb081d)


[查看生成文档示例](https://example.com/sample-docs)

## 项目结构

Lua Documentation Generator 采用模块化设计，主要包括以下部分：

- `src/`: 核心源代码
  - `lua_parser/`: Lua 代码解析器
  - `doc_generator/`: 文档生成器
  - `utils/`: 工具函数
  - `exceptions/`: 自定义异常类
- `tests/`: 单元测试和集成测试
- `templates/`: 文档模板
- `docs/`: 项目文档
- `examples/`: 示例 Lua 项目
- `scripts/`: 实用脚本

详细的项目结构和说明请参阅 [项目结构文档](docs/project_structure.md)。

## 安装

### 系统要求

- Python 3.7+
- pip
- Git (可选，用于版本控制功能)

### 安装步骤

1. 克隆仓库：
   ```
   git clone https://github.com/your-username/lua-doc-generator.git
   cd lua-doc-generator
   ```

2. 安装依赖：
   ```
   ./scripts/install_dependencies.sh
   ```

详细安装指南请参阅 [安装文档](docs/installation.md)。

## 使用指南

### 命令行参数

```
lua-doc-generator [OPTIONS] PROJECT_PATH
```

主要选项：
- `-o, --output FILE`: 输出文件名
- `-c, --config FILE`: 配置文件路径
- `-t, --template FILE`: 自定义模板文件路径
- `--coverage`: 生成覆盖率报告

### 文档注释格式

```lua
---这是一个示例函数
---@param name string 用户名
---@return string 问候语
function greet(name)
    return "Hello, " .. name
end
```

更多示例和详细说明请参阅 [使用指南](docs/usage.md)。

## 配置

`config.yaml` 文件支持多种选项，包括：

- `project_name`: 项目名称
- `file_extensions`: 要处理的文件扩展名
- `include_params`: 是否包含参数文档
- `include_returns`: 是否包含返回值文档
- `syntax_highlight`: 是否启用语法高亮

完整配置选项请查看 [配置文档](docs/configuration.md)。

## 高级功能

- 多文件模块支持
- 类型索引生成
- 版本控制集成
- 文档覆盖率报告

详细信息请参阅 [高级功能文档](docs/advanced-features.md)。

## 自定义模板

使用 Jinja2 模板引擎自定义文档输出格式。示例：

```markdown
# {{ project_name }} Documentation

{% for module_name, module_info in modules.items() %}
## {{ module_name }}

{{ module_info.description }}

{% for func in module_info.functions %}
### {{ func.name }}

{{ func.description }}
{% endfor %}
{% endfor %}
```

更多模板示例和说明请查看 [模板指南](docs/templates.md)。

## 安全考虑

1. **代码执行**: 本工具不会执行任何 Lua 代码。
2. **敏感信息**: 请勿在文档注释中包含敏感信息。
3. **输入验证**: 所有用户输入都经过严格验证。

更多安全建议请参阅 [安全指南](docs/security.md)。

## 故障排除与FAQ

常见问题：

1. **Q**: 如何处理大型项目的性能问题？
   **A**: 使用增量生成功能，仅处理更改的文件。

2. **Q**: 支持多语言文档生成吗？
   **A**: 目前不直接支持，但可以使用多个配置文件和模板来实现。

更多问题和解答请查看 [FAQ 和故障排除指南](docs/troubleshooting.md)。

## 与其他工具的比较

| 特性 | Lua Documentation Generator | LuaDoc | LDoc |
|------|---------------------------|--------|------|
| 多格式输出 | ✅ | ❌ | ✅ |
| 类型注解 | ✅ | ❌ | ✅ |
| 自定义模板 | ✅ | ❌ | ✅ |
| 覆盖率报告 | ✅ | ❌ | ❌ |
| 维护活跃度 | 高 | 低 | 中 |

## 贡献指南

我们欢迎各种形式的贡献！如何参与：

1. Fork 项目仓库
2. 创建您的特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

详细指南请查看 [贡献指南](CONTRIBUTING.md)。

## 路线图

- [x] 基本的 Markdown 文档生成
- [x] HTML 和 PDF 输出支持
- [ ] 增量文档生成
- [ ] 插件系统
- [ ] 交互式 HTML 文档
- [ ] IDE 集成插件

完整路线图请参阅 [项目路线图](ROADMAP.md)。

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。

---
