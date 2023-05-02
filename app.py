import openai
import os
from flask import Flask, request, jsonify

# 设置 OpenAI API 密钥
openai.api_key = os.environ.get("YOUR_API_KEY")

# 初始化 Flask 应用程序
app = Flask(__name__)

# 定义 Flask 路由
@app.route('/<string:word>')
def generate_text(word):

    # 获取生成文本的参数
    prompt = request.args.get(word)
    length = 500

    # 使用 OpenAI API 生成文本
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=200
    )

    # 返回生成的文本
    return jsonify({'text': response['choices'][0]['text']})

if __name__ == "__main__":
    port = int(os.environ.get("PORT"))
    app.run(host="0.0.0.0", port=port)