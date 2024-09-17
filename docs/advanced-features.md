# Lua Documentation Generator 高级功能

## 1. 多文件模块支持

处理跨多个文件的复杂模块结构：

```yaml
multi_file_modules:
  - name: core
    files:
      - src/core/init.lua
      - src/core/utils.lua
```

## 2. 类型索引生成

启用 `include_type_index: true` 在配置中，生成一个包含所有使用的类型及其位置的索引。

## 3. 版本控制集成

使用 Git 标签自动管理文档版本：

```yaml
use_git_version: true
```

## 4. 文档覆盖率报告

运行时添加 `--coverage` 参数生成覆盖率报告：

```bash
lua-doc-generator /path/to/project --coverage
```

## 5. 自定义模板

使用 `-t` 参数指定自定义 Jinja2 模板：

```bash
lua-doc-generator /path/to/project -t my_template.md.j2
```

## 6. 插件系统

开发插件来扩展功能（开发中）：

```python
class MyPlugin(Plugin):
    def process_function(self, func_info):
        # 自定义处理逻辑
        pass
```

## 7. 增量文档生成

仅处理自上次生成以来更改的文件（开发中）：

```bash
lua-doc-generator /path/to/project --incremental
```

## 8. 国际化支持

支持多语言文档注释：

```lua
---[en] This is an example function
---[zh] 这是一个示例函数
function example()
    -- 函数实现
end
```

## 9. IDE 集成

为常见 IDE 开发插件，实现无缝文档生成（计划中）。

## 10. 交互式 HTML 输出

生成包含可折叠部分、搜索功能的交互式 HTML 文档（开发中）。

每个高级功能的详细使用说明，请参阅各自的专业文档。