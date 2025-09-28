"""
搜索历史组件
类似Vue3的组件概念，封装搜索历史相关的UI和逻辑
"""

import streamlit as st
from datetime import datetime
from typing import List, Dict, Optional
from search_history import search_history


class SearchHistoryComponent:
    """搜索历史组件类"""
    
    def __init__(self, max_display_items: int = 10):
        self.max_display_items = max_display_items
    
    def render_sidebar(self):
        """渲染侧边栏的搜索历史部分"""
        with st.sidebar:
            st.subheader("搜索历史")
            
            # 清空历史按钮
            if st.button("🗑️ 清空历史", help="清空所有搜索历史记录"):
                search_history.clear_history()
                st.success("搜索历史已清空！")
                st.rerun()
            
            # 显示搜索统计
            stats = search_history.get_stats()
            st.metric("总搜索次数", stats['total_searches'])
            st.metric("不同关键词", stats['unique_keywords'])
            
            # 显示成功/失败搜索统计
            history = search_history.get_history()
            successful_searches = len([item for item in history if item.get('last_result_count', 0) > 0])
            failed_searches = len([item for item in history if item.get('last_result_count', 0) == 0])
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("✅ 成功", successful_searches)
            with col2:
                st.metric("❌ 失败", failed_searches)
            
            # 显示热门搜索
            popular_searches = search_history.get_popular_searches(limit=5)
            if popular_searches:
                st.markdown("**🔥 热门搜索:**")
                for item in popular_searches:
                    if st.button(
                        f"🔍 {item['keyword']}", 
                        key=f"popular_{item['keyword']}",
                        help=f"搜索次数: {item.get('search_count', 1)}"
                    ):
                        st.session_state['search_keyword'] = item['keyword']
                        st.rerun()
    
    def render_search_suggestions(self, query: str, limit: int = 5):
        """渲染搜索建议"""
        if not query or len(query) < 2:
            return
        
        suggestions = search_history.search_suggestions(query, limit=limit)
        if not suggestions:
            return
        
        st.markdown("💡 **搜索建议:**")
        suggestion_cols = st.columns(len(suggestions))
        
        for i, suggestion in enumerate(suggestions):
            with suggestion_cols[i]:
                if st.button(
                    f"🔍 {suggestion}", 
                    key=f"suggestion_{i}", 
                    help=f"搜索: {suggestion}"
                ):
                    st.session_state['search_keyword'] = suggestion
                    st.rerun()
    
    def render_history_cards(self):
        """渲染搜索历史卡片"""
        history = search_history.get_history(limit=self.max_display_items)
        
        if not history:
            return
        
        st.markdown("### 📚 搜索历史")
        
        # 创建两列布局显示搜索历史
        cols = st.columns(2)
        
        for i, item in enumerate(history):
            col_idx = i % 2
            with cols[col_idx]:
                self._render_history_card(item, i)
    
    def _render_history_card(self, item: Dict, index: int):
        """渲染单个历史记录卡片"""
        # 格式化时间显示
        try:
            last_searched = datetime.fromisoformat(item['last_searched'])
            time_str = last_searched.strftime("%m-%d %H:%M")
        except:
            time_str = "未知时间"
        
        # 判断搜索状态
        result_count = item.get('last_result_count', 0)
        if result_count > 0:
            status_icon = "✅"
            status_color = "#28a745"  # 绿色
            status_text = f"{result_count}个结果"
        else:
            status_icon = "❌"
            status_color = "#dc3545"  # 红色
            status_text = "搜索失败"
        
        # 创建搜索历史卡片
        with st.container():
            st.markdown(f"""
            <div style="
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 10px;
                margin: 5px 0;
                background-color: #f8f9fa;
                cursor: pointer;
                transition: all 0.3s ease;
            ">
                <div style="font-weight: bold; color: #333; font-size: 14px;">
                    {item['keyword']}
                </div>
                <div style="font-size: 0.8em; color: #666; margin-top: 5px;">
                    🔍 {item.get('search_count', 1)}次 | 
                    📅 {time_str} | 
                    <span style="color: {status_color}; font-weight: bold;">
                        {status_icon} {status_text}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 添加点击搜索功能
            if st.button(
                f"🔍 搜索", 
                key=f"history_search_{index}", 
                help=f"重新搜索: {item['keyword']}"
            ):
                st.session_state['search_keyword'] = item['keyword']
                st.rerun()
    
    def add_search_record(self, keyword: str, result_count: int = 0):
        """添加搜索记录"""
        search_history.add_search(keyword, result_count)
    
    def get_search_keyword_from_session(self) -> str:
        """从session state获取搜索关键词"""
        keyword = st.session_state.get('search_keyword', '')
        if keyword:
            # 清除session state中的搜索关键词
            del st.session_state['search_keyword']
        return keyword
    
    def render_search_input(self, placeholder: str = "请输入搜索关键词..."):
        """渲染搜索输入框"""
        # 检查是否有来自历史记录的搜索
        default_keyword = self.get_search_keyword_from_session()
        
        search_keyword = st.text_input(
            "🔍 请输入搜索关键词",
            value=default_keyword,
            placeholder=placeholder,
            help="输入您想要搜索的视频关键词"
        )
        
        # 显示搜索建议
        if search_keyword and len(search_keyword) >= 2:
            self.render_search_suggestions(search_keyword)
        
        return search_keyword


# 创建全局搜索历史组件实例
search_history_component = SearchHistoryComponent()
