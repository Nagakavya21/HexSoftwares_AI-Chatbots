# HexSoftwares_AI-Chatbot

🎥 Project Demo Video: Click to Watch

🤖 Chatter Box – AI-Chatbot Development

Chatter Box is a web-based chatbot application designed to interact with users in real-time, answer queries, and provide quick support in a human-like conversational style.
It is lightweight, fast, and accessible, making it suitable for websites, customer support portals, and interactive platforms.

📌 Main Features

Customer Support & Engagement

Works as a virtual assistant to answer user questions.

Keeps the conversation smooth and interactive.

Rule-Based NLP Processing

Uses keyword matching to understand and reply.

Does not require heavy ML models, ensuring fast performance.

Voice Interaction

Supports voice input through the Web Speech API.

Can optionally speak replies using text-to-speech.

Emoji Support

Includes an emoji picker for fun and expressive chats.

Responsive & Accessible Design

Works perfectly on mobile, tablet, and desktop.

Includes ARIA roles, live region updates, and keyboard navigation for accessibility.

🛠 Technologies & Techniques Used
💻Frontend

HTML5, CSS3, Vanilla JavaScript

Responsive UI with Flexbox & Media Queries

CSS Variables for easy theme customization (--primary, --secondary)

Animated typing indicators using @keyframes

DOM Manipulation to dynamically display messages

Web Speech API (Speech-to-Text)

SpeechSynthesis API (Text-to-Speech)

Emoji picker integration

XSS prevention with an escapeHtml() function

Backend

Python Flask (serves the app & handles chat logic)

Flask-CORS for API access

Rule-based NLP with keyword matching

Randomized responses using random.choice() for variety

Environment variables managed with python-dotenv

Structured logging using Python’s logging module

🚀 How It Works

User Interaction: User sends a message by typing, selecting an emoji, or using voice input.

Data Transfer: The message is sent to the Flask backend via Fetch API.

Processing: Backend applies rule-based NLP to understand and respond.

Response Delivery: A JSON response is sent back to the frontend.

Display & Voice Output: Chatbox shows the bot’s reply and optionally reads it aloud using text-to-speech.
