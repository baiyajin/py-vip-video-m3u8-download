#!/bin/bash

echo "正在启动VIP视频M3U8下载工具..."
echo

# 确保在正确的目录下运行
cd "$(dirname "$0")"

# 创建虚拟环境（如果不存在）
if [ ! -d ".venv" ]; then
    echo "创建虚拟环境..."
    python -m venv .venv
fi

# 激活虚拟环境
echo "激活虚拟环境..."
source .venv/bin/activate

# 检查依赖是否已安装
if [ ! -f ".venv/bin/streamlit" ]; then
    echo "正在安装依赖..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "错误: 依赖安装失败"
        exit 1
    fi
    echo "依赖安装成功！"
else
    echo "依赖已安装，跳过安装步骤"
fi

# 启动应用
echo "正在启动应用..."
echo ""
echo "========================================"
echo "🎬 VIP视频M3U8下载工具"
echo "========================================"
echo ""
echo "📱 应用将在浏览器中自动打开"
echo "🌐 如果没有自动打开，请手动访问: http://localhost:8501"
echo ""
echo "⚠️  按 Ctrl+C 可以停止应用"
echo "========================================"
echo ""

streamlit run main.py
