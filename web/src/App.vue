<template>
  <div class="min-h-screen bg-gray-50">
    <!-- 头部 -->
    <header class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <h1 class="text-2xl font-bold text-gray-900">
                VIP视频M3U8下载工具
              </h1>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <span class="text-sm text-gray-500">
              基于 Vue3 + Vite7 + UnoCSS 构建
            </span>
          </div>
        </div>
      </div>
    </header>

    <!-- 主内容 -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="text-center">
        <h2 class="text-3xl font-bold text-gray-900 mb-4">欢迎使用VIP视频M3U8下载工具</h2>
        <p class="text-lg text-gray-600 mb-8">基于 Vue3 + Vite7 + UnoCSS 构建的现代化视频搜索下载工具</p>
        
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-8">
          <h3 class="text-xl font-semibold text-gray-900 mb-4">功能特点</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <div class="p-4 border border-gray-200 rounded-lg">
              <div class="text-2xl mb-2">🔍</div>
              <h4 class="font-medium text-gray-900">智能搜索</h4>
              <p class="text-sm text-gray-600">支持关键词搜索视频资源</p>
            </div>
            <div class="p-4 border border-gray-200 rounded-lg">
              <div class="text-2xl mb-2">📚</div>
              <h4 class="font-medium text-gray-900">搜索历史</h4>
              <p class="text-sm text-gray-600">本地存储搜索记录</p>
            </div>
            <div class="p-4 border border-gray-200 rounded-lg">
              <div class="text-2xl mb-2">💡</div>
              <h4 class="font-medium text-gray-900">搜索建议</h4>
              <p class="text-sm text-gray-600">基于历史记录的智能建议</p>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- 页脚 -->
    <footer class="bg-white border-t border-gray-200 mt-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="text-center text-sm text-gray-500">
          <p>视频搜索下载工具 | 基于 Vue3 + Vite7 + UnoCSS 构建</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
// 简单的欢迎页面
</script>