# 初始化项目环境
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# 设置环境变量模板
Copy-Item .env.example .env
code .env  # 打开编辑器填写配置

Write-Host "✅ 项目初始化完成" -ForegroundColor Green
