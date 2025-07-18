# src/main.py 新增内容
from utils.helpers import setup_logging, validate_env_file

# 初始化配置
setup_logging()
validate_env_file()

# 原有代码...
import os
import logging

# 初始化日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_environment():
    """验证必需的环境变量"""
    required_keys = [
        'CRAWL4AI_KEY',
        'JINA_KEY', 
        'API_KEY'  # 根据您实际使用的API调整
    ]
    
    missing_keys = []
    for key in required_keys:
        if not os.getenv(key):
            missing_keys.append(key)
    
    if missing_keys:
        error_msg = f"缺少必需环境变量: {', '.join(missing_keys)}"
        logging.critical(error_msg)
        raise ValueError(error_msg)
    else:
        logging.info("所有环境变量验证通过")

# 程序启动时立即检查
validate_environment()                                                                                                      import os

# 检查环境变量
if not os.getenv("CRAWL4AI_KEY"):
    raise ValueError("请先在.env文件中配置CRAWL4AI_KEY")
# -*- coding: utf-8 -*-
print("=== 脚本初始化成功 ===")

def main():
    """主函数"""
    print("主程序运行正常")
    return True

if __name__ == "__main__":
    main()
import os
from pathlib import Path

if not Path('.env').exists():
    raise RuntimeError('缺少.env文件！请复制.env.example并配置')

from dotenv import load_dotenv
load_dotenv()

REQUIRED_KEYS = ['CRAWL4AI_KEY', 'JINA_KEY']
missing = [k for k in REQUIRED_KEYS if not os.getenv(k)]
if missing:
    raise ValueError(f'缺少环境变量: {missing}')
