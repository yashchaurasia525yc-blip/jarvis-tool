from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

@app.route("/jarvis", methods=["POST"])
def jarvis():
    data = request.json
    user_command = data.get("command", "")
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3.2-3b-instruct:free",
            "messages": [
                {"role": "system", "content": "You are Jarvis AI assistant. Answer concisely."},
                {"role": "user", "content": user_command}
            ]
        }
    )
    result = response.json()
    if "choices" in result:
        answer = result["choices"][0]["message"]["content"]
    else:
        answer = str(result)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
