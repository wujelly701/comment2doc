#!/bin/bash

# 定义颜色代码
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 检查Python版本
check_python_version() {
    if command -v python3 &>/dev/null; then
        python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
        if [ "$(echo "$python_version >= 3.7" | bc)" -eq 1 ]; then
            echo -e "${GREEN}Python $python_version 已安装${NC}"
        else
            echo -e "${RED}需要 Python 3.7 或更高版本。当前版本: $python_version${NC}"
            exit 1
        fi
    else
        echo -e "${RED}未找到 Python 3。请安装 Python 3.7 或更高版本。${NC}"
        exit 1
    fi
}

# 安装Python依赖
install_python_dependencies() {
    echo "正在安装 Python 依赖..."
    pip3 install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Python 依赖安装成功${NC}"
    else
        echo -e "${RED}Python 依赖安装失败${NC}"
        exit 1
    fi
}

# 安装wkhtmltopdf
install_wkhtmltopdf() {
    echo "正在检查 wkhtmltopdf..."
    if command -v wkhtmltopdf &>/dev/null; then
        echo -e "${GREEN}wkhtmltopdf 已安装${NC}"
    else
        echo "正在安装 wkhtmltopdf..."
        if [ "$(uname)" == "Darwin" ]; then
            # macOS
            brew install wkhtmltopdf
        elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
            # Linux
            if [ -f /etc/debian_version ]; then
                # Debian/Ubuntu
                sudo apt-get update
                sudo apt-get install -y wkhtmltopdf
            elif [ -f /etc/redhat-release ]; then
                # CentOS/RHEL
                sudo yum install -y wkhtmltopdf
            else
                echo -e "${RED}不支持的 Linux 发行版，请手动安装 wkhtmltopdf${NC}"
                exit 1
            fi
        else
            echo -e "${RED}不支持的操作系统，请手动安装 wkhtmltopdf${NC}"
            exit 1
        fi

        if [ $? -eq 0 ]; then
            echo -e "${GREEN}wkhtmltopdf 安装成功${NC}"
        else
            echo -e "${RED}wkhtmltopdf 安装失败${NC}"
            exit 1
        fi
    fi
}

# 主函数
main() {
    echo "开始安装 Lua Documentation Generator 依赖..."

    check_python_version
    install_python_dependencies
    install_wkhtmltopdf

    echo -e "${GREEN}所有依赖安装完成！${NC}"
}

# 运行主函数
main