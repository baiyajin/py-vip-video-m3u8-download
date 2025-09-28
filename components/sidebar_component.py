"""
侧边栏组件
封装侧边栏的显示逻辑
"""

import streamlit as st
from config import get_config


class SidebarComponent:
    """侧边栏组件类"""
    
    def __init__(self):
        self.app_config = get_config('app')
        self.search_config = get_config('search')
    
    def render_sidebar(self, search_history_component):
        """渲染侧边栏"""
        with st.sidebar:
            st.header("🔧 设置")
            
            # 搜索设置
            self._render_search_settings()
            
            # 显示设置
            self._render_display_settings()
            
            # 搜索历史管理
            search_history_component.render_sidebar()
            
            # 关于信息
            self._render_about_section()
    
    def _render_search_settings(self):
        """渲染搜索设置"""
        st.subheader("搜索设置")
        
        search_limit = st.slider(
            "搜索结果数量", 
            5, 50, 20,
            help="设置每次搜索返回的结果数量"
        )
        
        # 将搜索限制保存到session state
        st.session_state['search_limit'] = search_limit
    
    def _render_display_settings(self):
        """渲染显示设置"""
        st.subheader("显示设置")
        
        show_details = st.checkbox(
            "显示详细信息", 
            value=True,
            help="是否显示视频的详细信息"
        )
        
        auto_refresh = st.checkbox(
            "自动刷新", 
            value=False,
            help="是否自动刷新搜索结果"
        )
        
        # 保存显示设置到session state
        st.session_state['show_details'] = show_details
        st.session_state['auto_refresh'] = auto_refresh
    
    def _render_about_section(self):
        """渲染关于信息"""
        st.markdown("---")
        st.markdown("### 📖 关于")
        st.markdown("""
        这是一个基于Streamlit的VIP视频搜索工具，支持搜索和下载m3u8格式的视频。
        
        **主要功能：**
        - 🔍 智能搜索
        - 📚 搜索历史
        - 💡 搜索建议
        - 📱 响应式设计
        """)


# 创建全局侧边栏组件实例
sidebar_component = SidebarComponent()
