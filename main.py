import streamlit as st
import json
from typing import Dict, List, Optional
from api_client import api_client
from config import get_config, get_env_config
from components import search_history_component, video_card_component, sidebar_component

# 获取配置
app_config = get_config('app')
ui_config = get_config('ui')
search_config = get_config('search')

# 配置页面
st.set_page_config(
    page_title=app_config['title'],
    page_icon=app_config['icon'],
    layout=app_config['layout'],
    initial_sidebar_state=app_config['initial_sidebar_state']
)

# 这些函数已经被组件化，不再需要在这里定义

def main():
    """主函数"""
    st.title(f"{app_config['icon']} {app_config['title']}")
    st.markdown("---")
    
    # 渲染侧边栏组件
    sidebar_component.render_sidebar(search_history_component)
    
    # 主搜索区域
    st.markdown("🔍 请输入搜索关键词")
    
    # 使用更精确的列宽比例来确保对齐
    col1, col2 = st.columns([5, 1])
    
    with col1:
        # 使用搜索历史组件渲染搜索输入框（不显示标签）
        search_keyword = search_history_component.render_search_input(
            placeholder="例如：吴邪私家笔记、电影名称等..."
        )
    
    with col2:
        # 添加一些顶部间距来对齐按钮
        st.markdown("<br>", unsafe_allow_html=True)
        search_button = st.button("🔍 搜索", type="primary", use_container_width=True)
    
    # 搜索逻辑
    if search_button and search_keyword:
        # 获取搜索限制设置
        search_limit = st.session_state.get('search_limit', 20)
        
        with st.spinner("正在搜索，请稍候..."):
            result = api_client.search_videos(search_keyword, limit=search_limit)
            
            # 无论搜索成功还是失败，都记录搜索历史
            if result['success']:
                st.success(f"✅ {result['message']}")
                
                videos = result['data']
                result_count = len(videos) if videos else 0
                
                # 记录搜索历史（成功搜索）
                search_history_component.add_search_record(search_keyword, result_count)
                
                if videos:
                    st.markdown(f"### 📋 找到 {len(videos)} 个相关结果")
                    
                    # 使用视频卡片组件显示搜索结果
                    for i, video in enumerate(videos[:search_limit]):
                        video_card_component.render_video_card(video, i)
                        st.markdown("---")
                else:
                    st.warning("😔 没有找到相关结果，请尝试其他关键词")
            else:
                st.error(f"❌ 搜索失败: {result['error']}")
                
                # 记录搜索历史（失败搜索，结果数量为0）
                search_history_component.add_search_record(search_keyword, 0)
    
    elif search_button and not search_keyword:
        st.warning("⚠️ 请输入搜索关键词")
    
    # 使用搜索历史组件显示搜索历史
    search_history_component.render_history_cards()
    
    # 使用说明
    with st.expander("📖 使用说明"):
        st.markdown("""
        ### 如何使用这个工具：
        
        1. **搜索视频**: 在搜索框中输入关键词，如电影名称、演员名字等
        2. **查看结果**: 搜索结果会以卡片形式展示，包含视频的基本信息
        3. **操作视频**: 每个视频卡片都有观看、下载、收藏等操作按钮
        4. **调整设置**: 使用左侧边栏可以调整搜索数量和显示选项
        5. **搜索历史**: 查看和管理您的搜索历史记录
        6. **快速重搜**: 点击历史记录可以快速重新搜索
        
        ### 功能特点：
        - 🔍 智能搜索：支持多种关键词搜索
        - 📚 搜索历史：自动记录和管理搜索历史
        - 💡 搜索建议：输入时显示相关搜索建议
        - 📱 响应式设计：适配不同屏幕尺寸
        - ⚡ 快速加载：优化的网络请求
        - 🎨 美观界面：现代化的UI设计
        
        ### 搜索历史功能：
        - 📝 自动记录：每次搜索都会自动保存到历史记录（包括成功和失败）
        - 🔄 快速重搜：点击历史记录标题直接执行搜索
        - 📊 搜索统计：显示搜索次数、成功/失败统计
        - ✅ 状态显示：历史记录会显示搜索状态（成功/失败）
        - 🗑️ 清空历史：可以一键清空所有搜索历史
        - 💡 智能建议：输入时显示相关的历史搜索建议
        - 🔥 热门搜索：侧边栏显示热门搜索，点击直接搜索
        """)
    
    # 页脚
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "🎬 视频搜索下载工具 | 基于 Streamlit 构建"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
