/**
 * 搜索API服务
 */

const API_BASE_URL = '/api'

/**
 * 搜索视频
 * @param {string} keyword - 搜索关键词
 * @param {number} limit - 结果数量限制
 * @returns {Promise<Object>} 搜索结果
 */
export async function searchVideos(keyword, limit = 20) {
  try {
    const response = await fetch(`${API_BASE_URL}/search`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        keyword,
        limit
      })
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const data = await response.json()
    return data
  } catch (error) {
    console.error('搜索API错误:', error)
    throw error
  }
}

/**
 * 健康检查
 * @returns {Promise<Object>} 服务状态
 */
export async function healthCheck() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`)
    const data = await response.json()
    return data
  } catch (error) {
    console.error('健康检查失败:', error)
    throw error
  }
}
