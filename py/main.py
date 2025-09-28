"""
FastAPI后端服务
提供视频搜索API接口
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import requests
import uvicorn
from datetime import datetime

app = FastAPI(
    title="VIP视频M3U8下载工具 API",
    description="提供视频搜索和下载接口",
    version="1.0.0"
)

# 配置CORS，允许前端跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该设置具体的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求模型
class SearchRequest(BaseModel):
    keyword: str
    limit: Optional[int] = 20

class SearchResult(BaseModel):
    title: str
    url: str
    description: Optional[str] = None
    duration: Optional[str] = None
    thumbnail: Optional[str] = None

class SearchResponse(BaseModel):
    success: bool
    message: str
    data: List[SearchResult]
    total: int
    keyword: str
    search_time: str

# 搜索API
@app.post("/api/search", response_model=SearchResponse)
async def search_videos(request: SearchRequest):
    """搜索视频接口"""
    try:
        # 调用外部API
        api_url = "https://collect-v6.51.la/v6/collect"
        params = {
            "dt": 4,
            "keyword": request.keyword,
            "limit": request.limit
        }
        
        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()
        
        # 解析响应数据
        data = response.json()
        
        # 转换为标准格式
        results = []
        if isinstance(data, dict) and "data" in data:
            for item in data["data"]:
                results.append(SearchResult(
                    title=item.get("title", ""),
                    url=item.get("url", ""),
                    description=item.get("description", ""),
                    duration=item.get("duration", ""),
                    thumbnail=item.get("thumbnail", "")
                ))
        
        return SearchResponse(
            success=True,
            message="搜索成功",
            data=results,
            total=len(results),
            keyword=request.keyword,
            search_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"API请求失败: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"搜索失败: {str(e)}")

# 健康检查
@app.get("/api/health")
async def health_check():
    """健康检查接口"""
    return {"status": "ok", "message": "服务正常运行"}

# 根路径
@app.get("/")
async def root():
    """根路径"""
    return {"message": "VIP视频M3U8下载工具 API", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
