#!/bin/bash

echo "🎬 VIP视频M3U8下载工具"
echo "========================================"
echo ""
echo "📱 正在启动应用..."
echo "🌐 浏览器地址: http://localhost:8501"
echo ""
echo "⚠️  按 Ctrl+C 可以停止应用"
echo "========================================"
echo ""

# 确保在正确的目录下运行
cd "$(dirname "$0")"
streamlit run main.py --server.headless true --browser.gatherUsageStats false
