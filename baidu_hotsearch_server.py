from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup
from typing import List, Dict

mcp = FastMCP("百度热搜服务")

@mcp.tool()
def get_baidu_hotsearch() -> List[Dict[str, str]]:
    """获取百度热搜排行榜"""
    url = "https://top.baidu.com/board?tab=realtime"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        # 发送请求并解析页面
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取热搜标题和链接
        hot_list = []
        items = soup.select(".category-wrap_iQLoo")
        
        for item in items[:10]:  # 只取前10个热搜
            title_element = item.select_one(".c-single-text-ellipsis")
            if title_element:
                title = title_element.text.strip()
                # 构建搜索链接
                hot_list.append({"title": title})
        
        return hot_list if hot_list else [{"error": "未找到热搜数据"}]
    
    except Exception as e:
        return [{"error": f"数据获取失败: {str(e)}"}]

if __name__ == "__main__":
    mcp.run()