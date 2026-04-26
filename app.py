from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

@app.route("/jarvis", methods=["POST"])
def jarvis():
    data = request.json
    user_command = data.get("command", "")
    
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant. Answer concisely in 1-2 sentences only."},
                {"role": "user", "content": user_command}
            ]
        }
    )
    
    result = response.json()
    if "choices" in result:
        answer = result["choices"][0]["message"]["content"]
    else:
        answer = "Sorry, I could not process that."
    
    return answer, 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
