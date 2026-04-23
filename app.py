from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Apni API key yahan daalo
GEMINI_API_KEY = "AIzaSyAys-W_7Djd6g5hWfQGSO2RCYzb9_dWMAY"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/jarvis", methods=["POST"])
def jarvis():
    data = request.json
    user_command = data.get("command", "")
    
    if not user_command:
        return jsonify({"error": "No command given"}), 400
    
    response = model.generate_content(
        f"You are Jarvis, a helpful AI assistant. "
        f"Answer concisely. User said: {user_command}"
    )
    
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
