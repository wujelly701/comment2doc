# Lua Documentation Generator 安装指南

## 系统要求

- Python 3.7 或更高版本
- pip (Python 包管理器)
- Git (可选，用于版本控制功能)
- wkhtmltopdf (用于 PDF 生成，可选)

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/your-username/lua-doc-generator.git
cd lua-doc-generator
```

### 2. 创建虚拟环境（推荐）

```bash
python -m venv venv
source venv/bin/activate  # 在 Windows 上使用 venv\Scripts\activate
```

### 3. 安装依赖

使用提供的脚本安装所有依赖：

```bash
./scripts/install_dependencies.sh
```

或者手动安装：

```bash
pip install -r requirements.txt
```

### 4. 安装 wkhtmltopdf（可选，用于 PDF 生成）

- **Windows**: 从 [wkhtmltopdf 下载页面](https://wkhtmltopdf.org/downloads.html) 下载并安装
- **macOS**: `brew install wkhtmltopdf`
- **Linux**: `sudo apt-get install wkhtmltopdf` (Ubuntu/Debian)

### 5. 验证安装

运行以下命令验证安装：

```bash
python -m lua_doc_generator --version
```

如果安装成功，你应该看到版本号输出。

## 故障排除

- 如果遇到权限问题，尝试使用 `sudo` 运行安装命令。
- 确保你的 Python 版本兼容（使用 `python --version` 检查）。
- 对于 PDF 生成问题，确保 wkhtmltopdf 已正确安装并添加到系统路径。

如果你遇到任何其他问题，请查看我们的 [故障排除指南](troubleshooting.md) 或在 GitHub 上提交 issue。