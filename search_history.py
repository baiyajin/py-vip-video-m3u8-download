"""
搜索历史管理模块
提供搜索记录的存储、读取和管理功能
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from config import get_config


class SearchHistoryManager:
    """搜索历史管理器"""
    
    def __init__(self, history_file: str = "search_history.json"):
        self.history_file = history_file
        self.max_history = get_config('search').get('search_history_limit', 10)
        self.history = self._load_history()
    
    def _load_history(self) -> List[Dict]:
        """加载搜索历史"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get('history', [])
        except (json.JSONDecodeError, FileNotFoundError, KeyError):
            pass
        return []
    
    def _save_history(self):
        """保存搜索历史"""
        try:
            data = {
                'history': self.history,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存搜索历史失败: {e}")
    
    def add_search(self, keyword: str, result_count: int = 0):
        """添加搜索记录"""
        if not keyword or not keyword.strip():
            return
        
        keyword = keyword.strip()
        current_time = datetime.now()
        
        # 检查是否已存在相同的搜索
        for item in self.history:
            if item['keyword'].lower() == keyword.lower():
                # 更新现有记录
                item['last_searched'] = current_time.isoformat()
                item['search_count'] = item.get('search_count', 0) + 1
                item['last_result_count'] = result_count
                self._save_history()
                return
        
        # 添加新搜索记录
        new_item = {
            'keyword': keyword,
            'first_searched': current_time.isoformat(),
            'last_searched': current_time.isoformat(),
            'search_count': 1,
            'last_result_count': result_count
        }
        
        # 插入到列表开头
        self.history.insert(0, new_item)
        
        # 限制历史记录数量
        if len(self.history) > self.max_history:
            self.history = self.history[:self.max_history]
        
        self._save_history()
    
    def get_history(self, limit: Optional[int] = None) -> List[Dict]:
        """获取搜索历史"""
        if limit:
            return self.history[:limit]
        return self.history
    
    def clear_history(self):
        """清空搜索历史"""
        self.history = []
        self._save_history()
    
    def remove_search(self, keyword: str):
        """删除特定搜索记录"""
        self.history = [item for item in self.history if item['keyword'].lower() != keyword.lower()]
        self._save_history()
    
    def get_popular_searches(self, limit: int = 5) -> List[Dict]:
        """获取热门搜索（按搜索次数排序）"""
        sorted_history = sorted(
            self.history, 
            key=lambda x: x.get('search_count', 0), 
            reverse=True
        )
        return sorted_history[:limit]
    
    def search_suggestions(self, query: str, limit: int = 5) -> List[str]:
        """根据输入获取搜索建议"""
        if not query or len(query) < 2:
            return []
        
        query_lower = query.lower()
        suggestions = []
        
        for item in self.history:
            keyword = item['keyword']
            if query_lower in keyword.lower() and keyword not in suggestions:
                suggestions.append(keyword)
                if len(suggestions) >= limit:
                    break
        
        return suggestions
    
    def get_stats(self) -> Dict:
        """获取搜索统计信息"""
        if not self.history:
            return {
                'total_searches': 0,
                'unique_keywords': 0,
                'most_searched': None,
                'last_search': None
            }
        
        total_searches = sum(item.get('search_count', 0) for item in self.history)
        unique_keywords = len(self.history)
        
        most_searched = max(self.history, key=lambda x: x.get('search_count', 0))
        last_search = self.history[0] if self.history else None
        
        return {
            'total_searches': total_searches,
            'unique_keywords': unique_keywords,
            'most_searched': most_searched['keyword'] if most_searched else None,
            'last_search': last_search['keyword'] if last_search else None
        }


# 创建全局搜索历史管理器实例
search_history = SearchHistoryManager()
