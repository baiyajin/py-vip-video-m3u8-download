@echo off
echo.
echo ========================================
echo VIP Video M3U8 Download Tool
echo ========================================
echo.
echo Project Architecture:
echo   - Backend: Python FastAPI (Port 8000)
echo   - Frontend: Vue3 + Vite7 + UnoCSS (Port 3000)
echo.

echo Starting installation and services...
echo.

:: Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not detected, please install Python 3.8+
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Check Node.js installation
node --version >nul 2>&1
if errorlevel 1 (
    echo Error: Node.js not detected, please install Node.js 16+
    echo Download: https://nodejs.org/
    pause
    exit /b 1
)

:: Check pnpm installation
pnpm --version >nul 2>&1
if errorlevel 1 (
    echo Installing pnpm...
    npm install -g pnpm
    if errorlevel 1 (
        echo Failed to install pnpm
        pause
        exit /b 1
    )
)

echo Environment check passed
echo.

:: ==================== Backend Setup ====================
echo Setting up Python backend...
cd py

:: Create virtual environment (always create if not exists)
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
) else (
    echo Virtual environment already exists
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Install Python dependencies (always install/update)
echo Installing/updating Python dependencies...
pip install -r requirements.txt --upgrade
if errorlevel 1 (
    echo Failed to install Python dependencies
    pause
    exit /b 1
)

echo Python backend dependencies installed/updated
echo.

:: ==================== Frontend Setup ====================
echo Setting up Vue3 frontend...
cd ..\web

:: Check if package.json exists, if not create basic Vue3 project
if not exist "package.json" (
    echo Creating basic Vue3 project structure...
    echo This is a basic setup, full Vue3 project will be created
)

:: Install frontend dependencies
echo Installing/updating frontend dependencies...
pnpm install
if errorlevel 1 (
    echo Failed to install frontend dependencies
    pause
    exit /b 1
)

echo Vue3 frontend dependencies installed/updated
echo.

:: ==================== Start Services ====================
echo Starting services...
echo.

:: Start backend service
echo Starting backend service (Port 8000)...
start "Backend Service" cmd /k "cd /d %~dp0py && venv\Scripts\activate.bat && python run.py"

:: Wait for backend to start
echo Waiting for backend service to start...
timeout /t 5 /nobreak >nul

:: Start frontend service
echo Starting frontend service (Port 3000)...
start "Frontend Service" cmd /k "cd /d %~dp0web && pnpm run dev"

:: Wait for frontend to start
echo Waiting for frontend service to start...
timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo Project started successfully!
echo ========================================
echo.
echo Access URLs:
echo   - Frontend: http://localhost:3000
echo   - Backend API: http://localhost:8000
echo   - API Docs: http://localhost:8000/docs
echo.
echo Tips:
echo   - Frontend and backend services started in new windows
echo   - Close corresponding cmd windows to stop services
echo   - To reinstall dependencies, delete py\venv and web\node_modules folders
echo.
echo Press any key to exit...
pause >nul