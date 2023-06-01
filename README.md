# Description

一个雷神自动暂停程序

# Deployment
```angular2html
git clone https://github.com/twoonefour/leigod
cd leigod
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 Leigod.py >> log 2>&1
# 建议放入crontab，每天0点运行
```