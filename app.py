from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

@app.route("/jarvis", methods=["POST"])
def jarvis():
    data = request.json
    user_command = data.get("command", "")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key={GEMINI_API_KEY}"
    
    body = {"contents": [{"parts": [{"text": f"You are Jarvis AI assistant. Answer concisely. User said: {user_command}"}]}]}
    
    response = requests.post(url, json=body)
    result = response.json()
    answer = result["candidates"][0]["content"]["parts"][0]["text"]
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
