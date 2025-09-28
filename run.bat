@echo off
echo 正在启动VIP视频M3U8下载工具...
echo.

REM 确保在正确的目录下运行
cd /d "%~dp0"

REM 创建虚拟环境（如果不存在）
if not exist ".venv" (
    echo 创建虚拟环境...
    python -m venv .venv
)

REM 激活虚拟环境
echo 激活虚拟环境...
call .venv\Scripts\activate

REM 检查依赖是否已安装
if not exist ".venv\Scripts\streamlit.exe" (
    echo 正在安装依赖...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo 错误: 依赖安装失败
        pause
        exit /b 1
    )
    echo 依赖安装成功！
) else (
    echo 依赖已安装，跳过安装步骤
)

REM 启动应用
echo 正在启动应用...
echo.
echo ========================================
echo 🎬 VIP视频M3U8下载工具
echo ========================================
echo.
echo 📱 应用将在浏览器中自动打开
echo 🌐 如果没有自动打开，请手动访问: http://localhost:8501
echo.
echo ⚠️  按 Ctrl+C 可以停止应用
echo ========================================
echo.

streamlit run main.py

pause
