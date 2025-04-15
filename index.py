from flask import Flask, request, jsonify, send_from_directory
import os
from open_webui import app as open_webui_app

app = Flask(__name__)

# 将open-webui的路由挂载到Flask应用
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return open_webui_app.handle_request(request)

# 添加必要的环境变量
os.environ['PORT'] = '3000'

# Vercel函数处理入口
def handler(request, **kwargs):
    return app(request, **kwargs)
