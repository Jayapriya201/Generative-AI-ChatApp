import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage

# Load environment variables
load_dotenv()

# Azure config
PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT")
AZURE_KEY_CREDENTIAL = os.getenv("AZURE_KEY_CREDENTIAL")

# Flask app
app = Flask(__name__)

# Azure chat client
chat_client = ChatCompletionsClient(
    endpoint=PROJECT_ENDPOINT,
    credential=AzureKeyCredential(AZURE_KEY_CREDENTIAL),
)

# Initial chat history (reset on new personality)
chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        user_input = data.get("prompt", "")
        personality = data.get("personality", None)

        if not user_input:
            return jsonify({"error": "Empty prompt"}), 400

        global chat_history

        # Set personality prompt on first message
        if personality:
            personality_prompts = {
                "friendly": "You are a helpful and friendly assistant. Always greet warmly and be supportive.",
                "professional": "You are a concise, polite, and highly professional assistant.",
                "joking": "You are a humorous assistant who jokes around but still answers questions correctly."
            }
            prompt = personality_prompts.get(personality, "You are a helpful assistant.")
            chat_history = [SystemMessage(prompt)]

        chat_history.append(UserMessage(user_input))
        response = chat_client.complete(
            model=MODEL_DEPLOYMENT,
            messages=chat_history
        )
        answer = response.choices[0].message.content
        chat_history.append(AssistantMessage(answer))

        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
