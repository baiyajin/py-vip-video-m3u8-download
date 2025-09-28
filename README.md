# 🎬 VIP视频M3U8下载工具

基于 **Python FastAPI** + **Vue3** + **Vite7** + **UnoCSS** 构建的现代化视频搜索下载工具。

## ✨ 功能特点

- 🔍 **智能搜索** - 支持关键词搜索视频资源
- 📚 **搜索历史** - 本地存储搜索记录，支持快速重新搜索
- 💡 **搜索建议** - 基于历史记录的智能搜索建议
- 🎨 **现代UI** - 使用UnoCSS原子化样式，响应式设计
- ⚡ **高性能** - 前后端分离，API接口快速响应
- 📱 **跨平台** - 支持Windows、macOS、Linux

## 🏗️ 项目架构

```
py-vip-video-m3u8-download/
├── py/                    # Python FastAPI 后端
│   ├── main.py           # 主应用文件
│   ├── run.py            # 启动脚本
│   └── requirements.txt  # Python依赖
├── web/                  # Vue3 前端
│   ├── src/
│   │   ├── components/   # Vue组件
│   │   ├── api/         # API服务
│   │   ├── composables/ # 组合式函数
│   │   └── main.js      # 入口文件
│   ├── package.json     # 前端依赖
│   └── vite.config.js   # Vite配置
├── start.bat             # 一键启动脚本
└── README.md            # 项目说明
```

## 🚀 快速开始

### 环境要求

- **Python 3.8+**
- **Node.js 16+**

### 一键启动

```bash
# Windows - 自动安装依赖并启动
start.bat
```

**脚本功能:**
- ✅ 自动检查Python和Node.js环境
- ✅ 自动创建Python虚拟环境
- ✅ 自动安装前后端依赖
- ✅ 自动启动后端和前端服务
- ✅ 自动打开浏览器访问应用

### 手动启动 (可选)

如果需要手动控制，可以分别启动：

#### 后端服务
```bash
cd py
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

#### 前端服务
```bash
cd web
pnpm install
pnpm run dev
```

## 🌐 访问地址

- **前端界面**: http://localhost:3000
- **后端API**: http://localhost:8000
- **API文档**: http://localhost:8000/docs

## 📖 使用说明

1. **搜索视频**
   - 在搜索框输入关键词
   - 点击搜索按钮或按回车键
   - 查看搜索结果

2. **搜索历史**
   - 所有搜索记录自动保存到本地
   - 点击历史记录可快速重新搜索
   - 支持清空历史记录

3. **搜索建议**
   - 输入关键词时会显示相关建议
   - 基于历史搜索记录生成

## 🛠️ 技术栈

### 后端
- **FastAPI** - 现代、快速的Python Web框架
- **Pydantic** - 数据验证和序列化
- **Uvicorn** - ASGI服务器
- **Requests** - HTTP客户端

### 前端
- **Vue 3** - 渐进式JavaScript框架
- **Vite 7** - 下一代前端构建工具
- **UnoCSS** - 原子化CSS引擎
- **Pinia** - Vue状态管理

## 📦 项目依赖

### 后端依赖 (py/requirements.txt)
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
requests==2.31.0
pydantic==2.5.0
```

### 前端依赖 (web/package.json)
```json
{
  "dependencies": {
    "vue": "^3.4.0",
    "pinia": "^2.1.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "unocss": "^0.58.0",
    "@vitejs/plugin-vue": "^5.0.0"
  }
}
```

## 🔧 开发说明

### API接口

#### 搜索视频
```http
POST /api/search
Content-Type: application/json

{
  "keyword": "搜索关键词",
  "limit": 20
}
```

#### 健康检查
```http
GET /api/health
```

### 前端组件

- `SearchComponent.vue` - 主搜索组件
- `SearchHistoryComponent.vue` - 搜索历史组件
- `useSearchHistory.js` - 搜索历史组合式函数

## 🐛 故障排除

1. **环境检查失败**
   - 确保已安装Python 3.8+和Node.js 16+
   - 检查环境变量PATH设置
   - 重启命令行窗口

2. **依赖安装失败**
   - 检查网络连接
   - 尝试使用国内镜像源
   - 删除py\venv和web\node_modules重新安装

3. **服务启动失败**
   - 确保端口8000和3000未被占用
   - 检查防火墙设置
   - 查看cmd窗口中的错误信息

4. **API调用失败**
   - 确保后端服务已启动
   - 检查浏览器控制台错误
   - 验证API接口地址

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

---

**注意**: 请确保在项目根目录下运行启动脚本，不要在子目录中运行。