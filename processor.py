from jina import Client
import json

# 初始化（↑↑↑ 这三行不要漏）
client = Client(api_key="jina_74ed0d0cc13b45bdb0dd644ea0d6ed86VLTl7FdVDXz_u-gEmgCX7_0p0J1Y")  # 粘贴时删除中文注释

# 加载爬取的数据
import os
import sys  # 新增这行

if not os.path.exists('scraped_data.json'):
    print("错误：请先运行 scraper.py 生成数据文件")
    sys.exit(1)  # 修改为sys.exit更规范

with open('scraped_data.json', 'r') as f:  # 按Shift+Enter换行
    data = json.load(f)  # 注意缩进对齐

# 分块处理
for item in data:  # 输入冒号后自动缩进
    response = client.post(...)  # 参数参考上文                                                                                                                                                                                                                            with open('llm_data.jsonl', 'w') as f:  # 注意是字母'l'不是数字'1'
    for chunk in processed_chunks:  # 用↑↓方向键移动光标
        f.write(json.dumps(chunk) + '\\n')  # 双反斜杠