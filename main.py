import openai
from flask import Flask, request, jsonify

# 初始化 Flask 应用程序
app = Flask(__name__)

# 定义 Flask 路由
@app.route('/', methods=['POST'])
def generate_text():

    return "good"

# 运行 Flask 应用程序
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')