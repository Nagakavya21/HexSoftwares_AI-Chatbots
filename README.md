# HexSoftwares_AI-Chatbot
🤖 Chatter Box

🎥 Demo Video: Watch Here

Chatter Box is an AI-powered chatbot web application built to provide instant responses, customer support, and human-like conversations in real time.
It combines rule-based NLP with voice interaction and an intuitive UI to make chatting smooth and engaging.

📌 Features

💬 Customer Support & Engagement – Acts as a virtual assistant, answering queries and maintaining conversational flow.

🧠 Rule-Based NLP – Uses keyword matching for intelligent responses without heavy ML models.

🎙 Voice Interaction – Supports voice input via Web Speech API and optional text-to-speech for bot replies.

😊 Emoji Support – Quick emoji picker for expressive conversations.

📱 Responsive UI – Works seamlessly on desktop, tablet, and mobile.

♿ Accessible Design – ARIA roles, live region updates, and keyboard-friendly navigation.

🛠 Technologies & Techniques Used
Frontend

HTML5, CSS3, JavaScript (Vanilla)

Responsive UI with Flexbox and Media Queries

CSS Variables for theming (--primary, --secondary)

Animated typing indicators with @keyframes typing

DOM Manipulation for real-time chat rendering

Web Speech API (Speech-to-Text)

SpeechSynthesis API (Text-to-Speech)

Emoji Picker integration

XSS Prevention using escapeHtml()

Backend

Python Flask for serving pages and chat processing

Flask-CORS for cross-origin API access

Rule-based NLP with keyword matching

Randomized Responses via random.choice()

Environment Variables with python-dotenv

Structured Logging with Python’s logging module

🚀 How It Works

User sends a message (text, emoji, or voice).

Frontend sends the message to Flask backend via Fetch API.

Backend processes it using rule-based NLP.

JSON response is sent back to the frontend.

Bot reply is displayed, optionally spoken aloud, and chat scrolls to the latest message.

📂 Project Structure
ChatterBox/
│
├── static/            # CSS, JS, and assets
├── templates/         # HTML files
├── app.py             # Flask backend
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
