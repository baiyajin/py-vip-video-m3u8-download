"""
组件模块初始化文件
类似Vue3的组件系统，提供统一的组件导入接口
"""

from .search_history_component import search_history_component
from .video_card_component import video_card_component
from .sidebar_component import sidebar_component

__all__ = [
    'search_history_component',
    'video_card_component', 
    'sidebar_component'
]
