# 💬 Azure AI Chat App

This is a simple web-based chatbot application built with **Flask** and powered by **Azure OpenAI**. It allows users to interact with an AI assistant that can adopt different personalities: *Friendly*, *Professional*, or *Joking*.

## 🚀 Features

- 🌐 Web interface with real-time chat
- 🧠 Powered by Azure OpenAI (`ChatCompletionsClient`)
- 🎭 Choose from three AI personalities:
  - 🤝 **Friendly** – Warm and helpful
  - 🧑‍💼 **Professional** – Polished and concise
  - 🤪 **Joking** – Humorous and witty
- 💬 Maintains chat history per session
- 🧪 Simple backend API using Flask
- 🔐 Environment-based configuration using `.env`

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python 3, Flask
- **AI Integration**: Azure AI (OpenAI)
- **Environment Management**: `python-dotenv`

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/azure-ai-chat-app.git
cd azure-ai-chat-app

pip install -r requirements.txt

PROJECT_ENDPOINT=https://<your-azure-endpoint>
MODEL_DEPLOYMENT=<your-deployment-name>
AZURE_KEY_CREDENTIAL=<your-azure-api-key>

python app.py






