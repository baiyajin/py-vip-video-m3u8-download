<template>
  <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
    <div class="flex items-center justify-between mb-4">
      <h3 class="text-lg font-semibold text-gray-900 flex items-center">
        <i class="i-mdi-history mr-2"></i>
        搜索历史
      </h3>
      <button
        @click="handleClear"
        class="btn-secondary text-sm px-3 py-1"
      >
        <i class="i-mdi-delete mr-1"></i>
        清空历史
      </button>
    </div>

    <div v-if="history.length === 0" class="text-center py-8 text-gray-500">
      <i class="i-mdi-magnify text-4xl mb-2"></i>
      <p>暂无搜索历史</p>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div
        v-for="(item, index) in history"
        :key="index"
        class="search-card p-3"
        @click="handleSearch(item.keyword)"
      >
        <div class="flex items-center justify-between mb-2">
          <h4 class="font-medium text-gray-900 truncate">
            {{ item.keyword }}
          </h4>
          <span class="text-xs text-gray-500">
            {{ formatTime(item.last_searched) }}
          </span>
        </div>
        
        <div class="flex items-center justify-between text-sm text-gray-600">
          <div class="flex items-center space-x-3">
            <span class="flex items-center">
              <i class="i-mdi-magnify mr-1"></i>
              {{ item.search_count }}次
            </span>
            <span class="flex items-center">
              <i class="i-mdi-calendar mr-1"></i>
              {{ formatDate(item.last_searched) }}
            </span>
          </div>
          
          <div class="flex items-center">
            <i 
              :class="item.last_result_count > 0 ? 'i-mdi-check-circle text-green-500' : 'i-mdi-close-circle text-red-500'"
              class="mr-1"
            ></i>
            <span :class="item.last_result_count > 0 ? 'text-green-600' : 'text-red-600'">
              {{ item.last_result_count > 0 ? '搜索成功' : '搜索失败' }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- 统计信息 -->
    <div v-if="history.length > 0" class="mt-4 pt-4 border-t border-gray-200">
      <div class="grid grid-cols-3 gap-4 text-center">
        <div>
          <div class="text-2xl font-bold text-gray-900">{{ totalSearches }}</div>
          <div class="text-sm text-gray-500">总搜索次数</div>
        </div>
        <div>
          <div class="text-2xl font-bold text-green-600">{{ successfulSearches }}</div>
          <div class="text-sm text-gray-500">成功搜索</div>
        </div>
        <div>
          <div class="text-2xl font-bold text-red-600">{{ failedSearches }}</div>
          <div class="text-sm text-gray-500">失败搜索</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

// Props
const props = defineProps({
  history: {
    type: Array,
    default: () => []
  }
})

// Emits
const emit = defineEmits(['search', 'clear'])

// 计算属性
const totalSearches = computed(() => {
  return props.history.reduce((sum, item) => sum + item.search_count, 0)
})

const successfulSearches = computed(() => {
  return props.history.filter(item => item.last_result_count > 0).length
})

const failedSearches = computed(() => {
  return props.history.filter(item => item.last_result_count === 0).length
})

// 方法
const handleSearch = (keyword) => {
  emit('search', keyword)
}

const handleClear = () => {
  if (confirm('确定要清空所有搜索历史吗？')) {
    emit('clear')
  }
}

const formatTime = (timestamp) => {
  const date = new Date(timestamp)
  return date.toLocaleTimeString('zh-CN', { 
    hour: '2-digit', 
    minute: '2-digit' 
  })
}

const formatDate = (timestamp) => {
  const date = new Date(timestamp)
  return date.toLocaleDateString('zh-CN', { 
    month: '2-digit', 
    day: '2-digit' 
  })
}
</script>
