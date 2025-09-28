/**
 * 搜索历史组合式函数
 * 使用 localStorage 存储搜索历史
 */

import { ref, watch } from 'vue'

const STORAGE_KEY = 'video_search_history'
const MAX_HISTORY_ITEMS = 50

// 响应式搜索历史数据
const searchHistory = ref([])

// 从 localStorage 加载搜索历史
const loadHistory = () => {
  try {
    const stored = localStorage.getItem(STORAGE_KEY)
    if (stored) {
      searchHistory.value = JSON.parse(stored)
    }
  } catch (error) {
    console.error('加载搜索历史失败:', error)
    searchHistory.value = []
  }
}

// 保存搜索历史到 localStorage
const saveHistory = () => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(searchHistory.value))
  } catch (error) {
    console.error('保存搜索历史失败:', error)
  }
}

// 添加搜索记录
const addToHistory = (keyword, resultCount = 0) => {
  const now = new Date().toISOString()
  
  // 查找是否已存在相同关键词
  const existingIndex = searchHistory.value.findIndex(item => item.keyword === keyword)
  
  if (existingIndex >= 0) {
    // 更新现有记录
    searchHistory.value[existingIndex] = {
      ...searchHistory.value[existingIndex],
      search_count: searchHistory.value[existingIndex].search_count + 1,
      last_searched: now,
      last_result_count: resultCount
    }
  } else {
    // 添加新记录
    const newItem = {
      keyword,
      search_count: 1,
      first_searched: now,
      last_searched: now,
      last_result_count: resultCount
    }
    
    searchHistory.value.unshift(newItem)
    
    // 限制历史记录数量
    if (searchHistory.value.length > MAX_HISTORY_ITEMS) {
      searchHistory.value = searchHistory.value.slice(0, MAX_HISTORY_ITEMS)
    }
  }
  
  // 按最后搜索时间排序
  searchHistory.value.sort((a, b) => new Date(b.last_searched) - new Date(a.last_searched))
}

// 清空搜索历史
const clearHistory = () => {
  searchHistory.value = []
}

// 获取热门搜索
const getPopularSearches = (limit = 10) => {
  return searchHistory.value
    .filter(item => item.last_result_count > 0) // 只包含成功的搜索
    .sort((a, b) => b.search_count - a.search_count) // 按搜索次数排序
    .slice(0, limit)
}

// 获取搜索建议
const getSearchSuggestions = (query, limit = 5) => {
  if (!query || query.length < 2) return []
  
  return searchHistory.value
    .filter(item => 
      item.keyword.toLowerCase().includes(query.toLowerCase()) &&
      item.keyword !== query
    )
    .slice(0, limit)
    .map(item => item.keyword)
}

// 监听搜索历史变化，自动保存
watch(searchHistory, saveHistory, { deep: true })

// 初始化时加载历史
loadHistory()

export function useSearchHistory() {
  return {
    searchHistory,
    addToHistory,
    clearHistory,
    getPopularSearches,
    getSearchSuggestions
  }
}
