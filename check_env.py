#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
import os
import sys
from pathlib import Path

def debug_file(path):
    print("=== File Debug Info ===")
    print(f"绝对路径: {path.resolve()}")
    print("Hex头3字节:", end=' ')
    try:
        with open(path, 'rb') as f:
            print(' '.join(f"{b:02x}" for b in f.read(3)))
    except Exception as e:
        print(f"读取失败: {e}")

def main():
    env_path = Path('.env')
    
    # 调试输出
    debug_file(env_path)
    
    # 安全加载（兼容BOM）
    try:
        with open(env_path, 'r', encoding='utf-8-sig') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    k,v = line.strip().split('=',1)
                    os.environ[k] = v
    except Exception as e:
        print(f"❌ 加载失败: {e}")
        return 1
        
    required = ['CRAWL4AI_KEY','JINA_KEY','API_KEY']
    missing = [k for k in required if k not in os.environ]
    
    if missing:
        print(f"❌ 缺少变量: {missing}")
        return 1
        
    print("✅ 验证通过")
    print("示例值:", os.environ['CRAWL4AI_KEY'][0] + "***" + os.environ['CRAWL4AI_KEY'][-1])
    return 0

if __name__ == "__main__":
    sys.exit(main())
