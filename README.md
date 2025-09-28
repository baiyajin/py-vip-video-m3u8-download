# 🎬 VIP视频M3U8下载工具

一个基于 Streamlit 的VIP视频搜索和M3U8下载工具，支持通过关键词搜索视频内容并展示搜索结果。

## ✨ 功能特点

- 🔍 **智能搜索**: 支持多种关键词搜索视频内容
- 📚 **搜索历史**: 自动记录和管理搜索历史，支持快速重搜
- 💡 **搜索建议**: 输入时显示相关搜索建议，提升搜索体验
- 📱 **响应式设计**: 适配不同屏幕尺寸的现代化UI
- ⚡ **快速加载**: 优化的网络请求和数据处理
- 🎨 **美观界面**: 基于 Streamlit 的现代化界面设计
- 📊 **详细信息**: 展示视频的完整信息，包括演员、导演、简介等
- 📈 **搜索统计**: 显示搜索次数和结果数量统计

## 🚀 快速开始

### 环境要求

- Python 3.8.1+
- pip

### 安装和运行

**Windows:**
```bash
# 1、创建虚拟环境
python -m venv .venv

# 2、激活虚拟环境
.venv\Scripts\activate

# 3、安装依赖
pip install -r requirements.txt

# 4、运行应用 (确保在项目根目录下运行)
streamlit run main.py
```

**注意**: 请确保在项目根目录 `py-vip-video-m3u8-download` 下执行这些命令，不要切换到其他目录。

**macOS/Linux:**
```bash
# 1、创建虚拟环境
python -m venv .venv

# 2、激活虚拟环境
source .venv/bin/activate

# 3、安装依赖
pip install -r requirements.txt

# 4、运行应用 (确保在项目根目录下运行)
streamlit run main.py
```

**注意**: 请确保在项目根目录 `py-vip-video-m3u8-download` 下执行这些命令，不要切换到其他目录。


应用将在浏览器中自动打开，默认地址为 `http://localhost:8501`

### 💡 运行方式说明

**为什么使用 `streamlit run main.py`？**

- `streamlit run`: 启动Streamlit开发服务器，提供Web界面
- `main.py`: 我们的主程序文件

**两种运行方式对比：**

| 命令 | 用途 | 界面 | 功能 |
|------|------|------|------|
| `streamlit run main.py` | 启动Web应用 | 🌐 浏览器界面 | 完整功能，支持交互 |
| `python main.py` | 直接运行脚本 | 💻 终端输出 | 仅显示文本，无交互 |

### 快速启动

**方式一：完整安装启动 (推荐)**
```bash
# Windows: 双击运行
run.bat

# Linux/macOS: 给脚本执行权限并运行
chmod +x run.sh
./run.sh
```

**方式二：快速启动 (已安装依赖)**
```bash
# Windows: 双击运行
start.bat

# Linux/macOS: 给脚本执行权限并运行
chmod +x start.sh
./start.sh
```

**方式三：手动启动**
```bash
# 激活虚拟环境后直接运行
streamlit run main.py
```

### 启动脚本说明

- **run.bat/run.sh**: 完整安装脚本，会自动检查并安装依赖
- **start.bat/start.sh**: 快速启动脚本，假设依赖已安装
- **手动启动**: 需要先激活虚拟环境

应用启动后会自动在浏览器中打开 `http://localhost:8501`

## 📖 使用说明

1. **搜索视频**: 在搜索框中输入关键词，如电影名称、演员名字等
2. **查看结果**: 搜索结果会以卡片形式展示，包含视频的基本信息
3. **操作视频**: 每个视频卡片都有观看、下载、收藏等操作按钮
4. **调整设置**: 使用左侧边栏可以调整搜索数量和显示选项

## 🛠️ 技术栈

- **前端框架**: Streamlit
- **组件化架构**: 类似Vue3的组件系统
- **HTTP客户端**: requests
- **数据处理**: pandas
- **HTML解析**: BeautifulSoup4
- **包管理**: pip

## 🏗️ 组件化架构

项目采用类似Vue3的组件化架构，将UI功能模块化为独立的组件：

### 📦 组件系统

**核心组件：**
- `SearchHistoryComponent` - 搜索历史组件
- `VideoCardComponent` - 视频卡片组件  
- `SidebarComponent` - 侧边栏组件

**组件特点：**
- 🔧 **独立性**: 每个组件封装自己的逻辑和UI
- 🔄 **可复用**: 组件可以在不同地方重复使用
- 🎯 **单一职责**: 每个组件只负责特定功能
- 🧩 **组合式**: 组件可以组合使用构建复杂界面

**组件使用方式：**
```python
# 导入组件
from components import search_history_component, video_card_component

# 使用组件
search_history_component.render_sidebar()
video_card_component.render_video_card(video, index)
```

## 📁 项目结构

```
py-vip-video-m3u8-download/
├── main.py                    # 主程序文件 (Streamlit UI)
├── api_client.py              # API客户端模块
├── config.py                  # 配置文件
├── search_history.py          # 搜索历史管理模块
├── test_api.py                # API测试脚本
├── components/                # 组件目录 (类似Vue3组件系统)
│   ├── __init__.py           # 组件模块初始化
│   ├── search_history_component.py  # 搜索历史组件
│   ├── video_card_component.py      # 视频卡片组件
│   └── sidebar_component.py         # 侧边栏组件
├── requirements.txt           # pip依赖文件
├── run.bat                   # Windows完整安装启动脚本
├── run.sh                    # Linux/macOS完整安装启动脚本
├── start.bat                 # Windows快速启动脚本
├── start.sh                  # Linux/macOS快速启动脚本
├── .streamlit/               # Streamlit配置目录
│   └── config.toml           # Streamlit配置文件
├── search_history.json        # 搜索历史数据文件 (自动生成)
├── README.md                 # 项目说明文档
└── a.txt                    # 原始说明文件
```

## 🔧 配置说明

### API配置

项目使用 `https://collect-v6.51.la/v6/collect?dt=4` 作为搜索API接口。

### 自定义配置

您可以在 `config.py` 中修改以下配置：

- `API_CONFIG`: API相关配置（URL、超时时间等）
- `APP_CONFIG`: 应用配置（标题、布局等）
- `UI_CONFIG`: 界面配置（主题、显示选项等）
- `SEARCH_CONFIG`: 搜索配置（默认关键词、历史记录等）

## 🐛 故障排除

### 常见问题

1. **API请求失败**
   - 检查网络连接
   - 确认API接口是否可用
   - 查看控制台错误信息

2. **搜索结果为空**
   - 尝试不同的关键词
   - 检查API响应格式
   - 确认搜索参数正确

3. **界面显示异常**
   - 刷新浏览器页面
   - 检查Streamlit版本兼容性
   - 查看终端错误日志

## 📝 开发说明

### 添加新功能

1. 在 `VideoSearchAPI` 类中添加新的API方法
2. 在 `main()` 函数中添加对应的UI组件
3. 更新 `display_video_card()` 函数以支持新的显示内容

### 自定义样式

Streamlit支持自定义CSS，您可以在 `main.py` 中添加：

```python
st.markdown("""
<style>
.custom-class {
    color: red;
}
</style>
""", unsafe_allow_html=True)
```

## 📄 许可证

本项目采用 MIT 许可证。详情请查看 LICENSE 文件。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📞 支持

如果您遇到任何问题或有建议，请通过以下方式联系：

- 提交 GitHub Issue
- 发送邮件到 developer@example.com

---

**注意**: 本项目仅用于学习和研究目的，请遵守相关法律法规和网站使用条款。VIP视频下载请确保您有相应的观看权限。
