#!/usr/bin/env python3
"""
启动FastAPI后端服务
"""

import uvicorn
from main import app

if __name__ == "__main__":
    print("🚀 启动FastAPI后端服务...")
    print("📡 API地址: http://localhost:8000")
    print("📚 API文档: http://localhost:8000/docs")
    print("🔄 按 Ctrl+C 停止服务")
    print("-" * 50)
    
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=True,  # 开发模式，代码变更自动重启
        log_level="info"
    )
