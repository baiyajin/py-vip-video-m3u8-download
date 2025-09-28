"""
视频卡片组件
封装视频卡片的显示逻辑
"""

import streamlit as st
from typing import Dict


class VideoCardComponent:
    """视频卡片组件类"""
    
    def __init__(self):
        self.default_thumbnail = "https://via.placeholder.com/200x300/4CAF50/FFFFFF?text=视频"
    
    def render_video_card(self, video: Dict, index: int):
        """渲染单个视频卡片"""
        with st.container():
            col1, col2 = st.columns([1, 3])
            
            with col1:
                # 视频缩略图
                st.image(
                    self.default_thumbnail, 
                    width=200, 
                    caption=f"视频 {index + 1}"
                )
            
            with col2:
                # 视频标题
                st.subheader(f"🎬 {video.get('title', '未知标题')}")
                
                # 基本信息
                self._render_basic_info(video)
                
                # 演员和导演信息
                self._render_crew_info(video)
                
                # 简介
                self._render_synopsis(video)
                
                # 操作按钮
                self._render_action_buttons(video, index)
    
    def _render_basic_info(self, video: Dict):
        """渲染基本信息"""
        col2_1, col2_2, col2_3 = st.columns(3)
        
        with col2_1:
            st.metric("类型", video.get('type', '未知'))
        
        with col2_2:
            st.metric("年份", video.get('year', '未知'))
        
        with col2_3:
            st.metric("语言", video.get('language', '未知'))
    
    def _render_crew_info(self, video: Dict):
        """渲染演员和导演信息"""
        if video.get('actors'):
            st.write(f"**主演:** {video.get('actors', '未知')}")
        
        if video.get('director'):
            st.write(f"**导演:** {video.get('director', '未知')}")
    
    def _render_synopsis(self, video: Dict):
        """渲染简介"""
        if video.get('synopsis'):
            with st.expander("剧情简介"):
                st.write(video.get('synopsis', '暂无简介'))
    
    def _render_action_buttons(self, video: Dict, index: int):
        """渲染操作按钮"""
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            if st.button(f"📺 观看", key=f"watch_{index}"):
                st.success("正在跳转到播放页面...")
        
        with col_btn2:
            if st.button(f"⬇️ 下载", key=f"download_{index}"):
                st.info("正在准备下载...")
        
        with col_btn3:
            if st.button(f"❤️ 收藏", key=f"favorite_{index}"):
                st.success("已添加到收藏夹")


# 创建全局视频卡片组件实例
video_card_component = VideoCardComponent()
