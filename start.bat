@echo off
chcp 65001 >nul
echo.
echo ========================================
echo 🎬 VIP视频M3U8下载工具
echo ========================================
echo.
echo 📋 项目架构:
echo   - 后端: Python FastAPI (端口 8000)
echo   - 前端: Vue3 + Vite7 + UnoCSS (端口 3000)
echo.

echo 🔧 开始安装和启动服务...
echo.

:: 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未检测到Python，请先安装Python 3.8+
    echo 📥 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: 检查Node.js是否安装
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未检测到Node.js，请先安装Node.js 16+
    echo 📥 下载地址: https://nodejs.org/
    pause
    exit /b 1
)

echo ✅ 环境检查通过
echo.

:: ==================== 后端设置 ====================
echo 📦 设置Python后端...
cd py

:: 创建虚拟环境
if not exist "venv" (
    echo 🔨 创建Python虚拟环境...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ 创建虚拟环境失败
        pause
        exit /b 1
    )
)

:: 激活虚拟环境
echo 🔧 激活虚拟环境...
call venv\Scripts\activate.bat

:: 安装Python依赖
echo 📥 安装Python依赖...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Python依赖安装失败
    pause
    exit /b 1
)

echo ✅ Python后端依赖安装完成
echo.

:: ==================== 前端设置 ====================
echo 📦 设置Vue3前端...
cd ..\web

:: 安装前端依赖
echo 📥 安装前端依赖...
npm install
if errorlevel 1 (
    echo ❌ 前端依赖安装失败
    pause
    exit /b 1
)

echo ✅ Vue3前端依赖安装完成
echo.

:: ==================== 启动服务 ====================
echo 🚀 启动服务...
echo.

:: 启动后端服务
echo 📡 启动后端服务 (端口 8000)...
start "后端服务" cmd /k "cd /d %~dp0py && venv\Scripts\activate.bat && python run.py"

:: 等待后端启动
echo ⏳ 等待后端服务启动...
timeout /t 5 /nobreak >nul

:: 启动前端服务
echo 🎨 启动前端服务 (端口 3000)...
start "前端服务" cmd /k "cd /d %~dp0web && npm run dev"

:: 等待前端启动
echo ⏳ 等待前端服务启动...
timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo ✅ 项目启动完成!
echo ========================================
echo.
echo 🌐 访问地址:
echo   - 前端界面: http://localhost:3000
echo   - 后端API: http://localhost:8000
echo   - API文档: http://localhost:8000/docs
echo.
echo 💡 提示:
echo   - 前端和后端服务已在新窗口中启动
echo   - 关闭对应的cmd窗口即可停止服务
echo   - 如需重新安装依赖，请删除 py\venv 和 web\node_modules 文件夹
echo.
echo 按任意键退出...
pause >nul
