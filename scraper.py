from crawl4ai.async_webcrawler import AsyncWebCrawler
import json
import asyncio

async def crawl():
    try:
        async with AsyncWebCrawler(token="YOUR_API_KEY") as crawler:
            result = await crawler.arun(
                url="https://example.com",
                strategy="main_content",
                output="markdown",
                timeout=30
            )
            
            # 提取数据并保存
            data = {
                "url": result.url,
                "markdown": result.markdown.raw_markdown if hasattr(result.markdown, 'raw_markdown') else str(result.markdown),
                "html": result.html,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            with open('scraped_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ 爬取成功！已保存 {len(data.get('markdown', ''))} 字符的Markdown内容")
    
    except Exception as e:
        print(f"❌ 错误: {str(e)}")

if __name__ == "__main__":
    import time
    start = time.time()
    asyncio.run(crawl())
    print(f"⏱ 总耗时: {time.time()-start:.2f}秒")
    import os
from typing import Optional

def get_api_key() -> Optional[str]:
    """安全获取API密钥"""
    key = os.getenv("CRAWL4AI_KEY")
    if not key:
        print("警告：未检测到CRAWL4AI_KEY环境变量")
    return key

# 使用示例
api_key = get_api_key()
if not api_key:
    # 处理密钥缺失情况
    raise RuntimeError("无法获取API密钥")