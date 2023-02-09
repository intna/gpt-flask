from flask import Flask,request
import openai

app = Flask("gpt")

@app.route("/chat")
def send():
    prompt = request.values.get("prompt")
    openai.api_key = "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"
    completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.6,
)
    message = completions.choices[0].text
    return message

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8999,debug=True)
