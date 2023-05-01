import openai
openai.api_key = "YOUR API KEY"
prompt = "你会Python开发吗？"
model = "text-davinci-002"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=60)
print(response.choices[0].text)