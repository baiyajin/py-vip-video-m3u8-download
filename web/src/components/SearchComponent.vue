<template>
  <div class="space-y-6">
    <!-- 搜索区域 -->
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
      <h2 class="text-lg font-semibold text-gray-900 mb-4">🔍 视频搜索</h2>
      
      <!-- 搜索输入框 -->
      <div class="flex gap-4">
        <div class="flex-1">
          <input
            v-model="searchKeyword"
            type="text"
            placeholder="例如：吴邪私家笔记、电影名称等..."
            class="input w-full"
            @keyup.enter="handleSearch"
          />
        </div>
        <button
          @click="handleSearch"
          :disabled="loading || !searchKeyword.trim()"
          class="btn-primary px-6 py-2 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <i class="i-mdi-magnify mr-2"></i>
          {{ loading ? '搜索中...' : '搜索' }}
        </button>
      </div>

      <!-- 搜索建议 -->
      <div v-if="searchSuggestions.length > 0" class="mt-4">
        <p class="text-sm text-gray-600 mb-2">💡 搜索建议:</p>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="suggestion in searchSuggestions"
            :key="suggestion"
            @click="selectSuggestion(suggestion)"
            class="btn-secondary text-sm px-3 py-1"
          >
            🔍 {{ suggestion }}
          </button>
        </div>
      </div>
    </div>

    <!-- 搜索结果 -->
    <div v-if="searchResults.length > 0" class="space-y-4">
      <div class="flex items-center justify-between">
        <h3 class="text-lg font-semibold text-gray-900">
          搜索结果 ({{ searchResults.length }} 个)
        </h3>
        <div class="text-sm text-gray-500">
          搜索时间: {{ searchTime }}
        </div>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div
          v-for="(video, index) in searchResults"
          :key="index"
          class="search-card"
          @click="handleVideoClick(video)"
        >
          <div class="aspect-video bg-gray-100 rounded-lg mb-3 flex items-center justify-center">
            <i class="i-mdi-play-circle text-4xl text-gray-400"></i>
          </div>
          <h4 class="font-medium text-gray-900 mb-2 line-clamp-2">
            {{ video.title }}
          </h4>
          <p v-if="video.description" class="text-sm text-gray-600 mb-2 line-clamp-2">
            {{ video.description }}
          </p>
          <div class="flex items-center justify-between text-xs text-gray-500">
            <span v-if="video.duration">
              <i class="i-mdi-clock mr-1"></i>
              {{ video.duration }}
            </span>
            <span class="text-primary-600 font-medium">点击查看详情</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 搜索历史 -->
    <SearchHistoryComponent
      v-if="searchHistory.length > 0"
      :history="searchHistory"
      @search="handleHistorySearch"
      @clear="clearHistory"
    />

    <!-- 错误信息 -->
    <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4">
      <div class="flex items-center">
        <i class="i-mdi-alert-circle text-red-500 mr-2"></i>
        <span class="text-red-700">{{ error }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import SearchHistoryComponent from './SearchHistoryComponent.vue'
import { searchVideos } from '../api/search'
import { useSearchHistory } from '../composables/useSearchHistory'

// 响应式数据
const searchKeyword = ref('')
const searchResults = ref([])
const loading = ref(false)
const error = ref('')
const searchTime = ref('')

// 搜索历史
const { searchHistory, addToHistory, clearHistory } = useSearchHistory()

// 搜索建议
const searchSuggestions = computed(() => {
  if (!searchKeyword.value || searchKeyword.value.length < 2) return []
  
  return searchHistory.value
    .filter(item => 
      item.keyword.toLowerCase().includes(searchKeyword.value.toLowerCase()) &&
      item.keyword !== searchKeyword.value
    )
    .slice(0, 5)
    .map(item => item.keyword)
})

// 搜索处理
const handleSearch = async () => {
  if (!searchKeyword.value.trim()) return
  
  loading.value = true
  error.value = ''
  
  try {
    const response = await searchVideos(searchKeyword.value.trim())
    
    if (response.success) {
      searchResults.value = response.data
      searchTime.value = response.search_time
      
      // 添加到搜索历史
      addToHistory(searchKeyword.value.trim(), response.data.length)
    } else {
      error.value = response.message || '搜索失败'
      // 即使失败也添加到历史
      addToHistory(searchKeyword.value.trim(), 0)
    }
  } catch (err) {
    error.value = '网络错误，请检查后端服务是否启动'
    console.error('搜索错误:', err)
    // 即使失败也添加到历史
    addToHistory(searchKeyword.value.trim(), 0)
  } finally {
    loading.value = false
  }
}

// 选择搜索建议
const selectSuggestion = (suggestion) => {
  searchKeyword.value = suggestion
  handleSearch()
}

// 历史搜索
const handleHistorySearch = (keyword) => {
  searchKeyword.value = keyword
  handleSearch()
}

// 视频点击处理
const handleVideoClick = (video) => {
  console.log('点击视频:', video)
  // 这里可以添加视频详情页面或下载逻辑
}

// 组件挂载时加载搜索历史
onMounted(() => {
  // 搜索历史会在 useSearchHistory 中自动加载
})
</script>
