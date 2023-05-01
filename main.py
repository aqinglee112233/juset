import openai
from flask import Flask, request, jsonify

# 设置 OpenAI API 密钥
openai.api_key = "YOUR_API_KEY"

# 初始化 Flask 应用程序
app = Flask(__name__)

# 定义 Flask 路由
@app.route('/', methods=['POST'])
def generate_text():
    # 从 POST 请求中获取请求体
    data = request.get_json()

    # 获取生成文本的参数
    prompt = data['prompt']
    length = data['length']

    # 使用 OpenAI API 生成文本
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=length
    )

    # 返回生成的文本
    return jsonify({'text': response['choices'][0]['text']})

# 运行 Flask 应用程序
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)