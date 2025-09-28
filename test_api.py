"""
API客户端测试脚本
用于测试视频搜索API的功能
"""

from api_client import api_client
import json


def test_search_api():
    """测试搜索API"""
    print("🧪 开始测试视频搜索API...")
    
    # 测试搜索功能
    test_keywords = ["吴邪私家笔记", "电影", "电视剧"]
    
    for keyword in test_keywords:
        print(f"\n🔍 测试关键词: {keyword}")
        result = api_client.search_videos(keyword)
        
        print(f"✅ 搜索成功: {result['success']}")
        print(f"📝 消息: {result['message']}")
        print(f"📊 结果数量: {len(result['data'])}")
        
        if result['data']:
            print("📋 前3个结果:")
            for i, video in enumerate(result['data'][:3]):
                print(f"  {i+1}. {video.get('title', '未知标题')}")
        
        if not result['success']:
            print(f"❌ 错误: {result.get('error', '未知错误')}")


def test_api_connection():
    """测试API连接"""
    print("🌐 测试API连接...")
    
    try:
        result = api_client.search_videos("test")
        if result['success']:
            print("✅ API连接正常")
        else:
            print(f"⚠️ API连接异常: {result.get('error', '未知错误')}")
    except Exception as e:
        print(f"❌ 连接失败: {str(e)}")


if __name__ == "__main__":
    print("🎬 VIP视频M3U8下载API测试工具")
    print("=" * 50)
    
    # 测试API连接
    test_api_connection()
    
    # 测试搜索功能
    test_search_api()
    
    print("\n" + "=" * 50)
    print("🏁 测试完成")
