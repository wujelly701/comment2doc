# Lua Documentation Generator 使用指南

## 基本用法

1. 在你的 Lua 项目根目录创建 `config.yaml` 文件。
2. 运行文档生成器：

```bash
lua-doc-generator /path/to/your/project -o output.md
```

## 命令行参数

- `PROJECT_PATH`: Lua 项目的路径（必需）
- `-o, --output FILE`: 输出文件名（默认：lua_api_docs.md）
- `-c, --config FILE`: 配置文件路径（默认：项目根目录的 config.yaml）
- `-t, --template FILE`: 自定义模板文件路径
- `-v, --verbose`: 启用详细输出
- `--coverage`: 生成覆盖率报告

## 文档注释格式

### 函数文档

```lua
---这是一个示例函数的描述
---@param name string 用户名
---@param age number 用户年龄
---@return string 问候语
---@usage local greeting = greet("Alice", 30)
function greet(name, age)
    return string.format("Hello, %s! You are %d years old.", name, age)
end
```

### 模块文档

```lua
---@module user_management
---这个模块提供了用户管理相关的功能

local user_management = {}

-- 模块中的函数定义...

return user_management
```

### 表文档

```lua
---用户配置表
---@field name string 用户名
---@field age number 用户年龄
---@field is_admin boolean 是否是管理员
local user_config = {
    name = "default_user",
    age = 0,
    is_admin = false
}
```

## 输出格式

- Markdown: 使用 `.md` 扩展名
- HTML: 使用 `.html` 扩展名
- PDF: 使用 `.pdf` 扩展名（需要安装 wkhtmltopdf）

## 最佳实践

1. 为所有公共函数和表编写文档注释。
2. 使用一致的文档格式和命名约定。
3. 提供清晰的参数和返回值描述。
4. 包含使用示例和代码片段。
5. 定期更新文档，确保与代码同步。

更多高级用法，请参阅 [高级功能文档](advanced-features.md)。