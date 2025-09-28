"""
项目配置文件
包含所有可配置的参数和设置
"""

import os
from typing import Dict, Any

# API配置
API_CONFIG = {
    'base_url': 'https://collect-v6.51.la/v6/collect',
    'timeout': 30,
    'retry_count': 3,
    'retry_delay': 1,
    'default_limit': 20,
    'max_limit': 100
}

# 应用配置
APP_CONFIG = {
    'title': 'VIP视频M3U8下载工具',
    'icon': '🎬',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
    'page_size': 20,
    'auto_refresh_interval': 30
}

# UI配置
UI_CONFIG = {
    'theme': {
        'primary_color': '#FF6B6B',
        'background_color': '#FFFFFF',
        'secondary_background_color': '#F0F2F6',
        'text_color': '#262730'
    },
    'display': {
        'show_video_thumbnails': True,
        'show_video_details': True,
        'show_actor_info': True,
        'show_director_info': True,
        'show_synopsis': True
    }
}

# 搜索配置
SEARCH_CONFIG = {
    'default_keywords': [
        '吴邪私家笔记',
        '电影',
        '电视剧',
        '综艺',
        '动漫'
    ],
    'search_history_limit': 20,
    'auto_complete': True,
    'fuzzy_search': True,
    'show_search_history': True,
    'history_display_limit': 10,
    'enable_search_suggestions': True
}

# 下载配置
DOWNLOAD_CONFIG = {
    'default_output_dir': './downloads',
    'supported_formats': ['mp4', 'mkv', 'avi', 'mov'],
    'max_concurrent_downloads': 3,
    'chunk_size': 8192
}

# 日志配置
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'app.log',
    'max_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5
}

# 缓存配置
CACHE_CONFIG = {
    'enabled': True,
    'ttl': 3600,  # 1小时
    'max_size': 100,
    'storage_type': 'memory'  # memory, redis, file
}

def get_config(section: str) -> Dict[str, Any]:
    """
    获取指定配置节
    
    Args:
        section: 配置节名称
        
    Returns:
        配置字典
    """
    configs = {
        'api': API_CONFIG,
        'app': APP_CONFIG,
        'ui': UI_CONFIG,
        'search': SEARCH_CONFIG,
        'download': DOWNLOAD_CONFIG,
        'log': LOG_CONFIG,
        'cache': CACHE_CONFIG
    }
    
    return configs.get(section, {})

def get_env_config() -> Dict[str, str]:
    """
    获取环境变量配置
    
    Returns:
        环境变量字典
    """
    return {
        'api_base_url': os.getenv('API_BASE_URL', API_CONFIG['base_url']),
        'debug_mode': os.getenv('DEBUG_MODE', 'False').lower() == 'true',
        'log_level': os.getenv('LOG_LEVEL', LOG_CONFIG['level']),
        'cache_enabled': os.getenv('CACHE_ENABLED', str(CACHE_CONFIG['enabled'])).lower() == 'true'
    }

# 导出配置
__all__ = [
    'API_CONFIG',
    'APP_CONFIG', 
    'UI_CONFIG',
    'SEARCH_CONFIG',
    'DOWNLOAD_CONFIG',
    'LOG_CONFIG',
    'CACHE_CONFIG',
    'get_config',
    'get_env_config'
]
