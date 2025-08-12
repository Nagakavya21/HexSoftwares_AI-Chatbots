# app.py (local only)
import os
import time
import random
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ChatterBox")

app = Flask(__name__, template_folder="templates")
CORS(app)

# Local fallback responses only
LOCAL_KNOWLEDGE = {
    "greetings": [
        "Hey there! I'm ChatterBox 🤖 — what’s on your mind?",
        "Hello! 😊 ChatterBox at your service.",
        "Hi! 👋 How can ChatterBox help you today?"
    ],
    "goodbye": [
        "Catch you later! 👋",
        "Goodbye from ChatterBox — take care!",
        "Bye-bye! Don’t be a stranger."
    ],
    "thanks": [
        "You’re most welcome! 🙌",
        "Anytime! That’s what I’m here for. 😊",
        "Glad I could help! 👍"
    ],
    "capabilities": [
        "I can answer general questions, help with coding tips, share fun facts, or just have a friendly chat.",
        "From solving small puzzles to chatting about big ideas — ChatterBox has got you covered!"
    ],
    "good_morning": [
        "Good morning! ☀ Wishing you a day full of smiles.",
        "Morning! Let’s make today awesome. 🌼"
    ],
    "good_night": [
        "Good night! 🌙 Sleep well and recharge.",
        "Sweet dreams! See you next time. ⭐"
    ],
    "joke": [
        "Why don’t skeletons fight each other? They don’t have the guts! 💀😂",
        "What do you call fake spaghetti? An impasta! 🍝🤣"
    ],
    "how_are_you": [
        "I’m feeling chatty and fantastic! How about you?",
        "I’m doing great, thanks! Always happy to talk."
    ],
    "default": [
        "That’s interesting — tell me more!",
        "Hmm… I don’t have the perfect answer, but I’d love to help figure it out.",
        "Let’s explore that together — what else can you share?"
    ],
    "error": [
        "Oops, something went wrong! Can we try again?",
        "Sorry, I hit a glitch there — let’s give it another shot."
    ]
}

def get_local_response(text):
    t = text.lower()
    if any(x in t for x in ["hi", "hello", "hey"]):
        return random.choice(LOCAL_KNOWLEDGE["greetings"])
    if any(x in t for x in ["bye", "goodbye", "see you"]):
        return random.choice(LOCAL_KNOWLEDGE["goodbye"])
    if any(x in t for x in ["thank", "thanks"]):
        return random.choice(LOCAL_KNOWLEDGE["thanks"])
    if "what can you" in t or "capabilities" in t:
        return random.choice(LOCAL_KNOWLEDGE["capabilities"])
    if "good morning" in t:
        return random.choice(LOCAL_KNOWLEDGE["good_morning"])
    if "good night" in t:
        return random.choice(LOCAL_KNOWLEDGE["good_night"])
    if "tell me a joke" in t:
        return random.choice(LOCAL_KNOWLEDGE["joke"])
    if "how are you" in t:
        return random.choice(LOCAL_KNOWLEDGE["how_are_you"])
    if "?" in t:
        return random.choice(LOCAL_KNOWLEDGE["default"])
    return random.choice(LOCAL_KNOWLEDGE["default"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    start_time = time.time()
    data = request.get_json(force=True, silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Empty message", "reply": "Please send a message."}), 400

    logger.info("User: %s", message)

    # Always use local responses
    reply = get_local_response(message)
    elapsed = round(time.time() - start_time, 2)
    logger.info("Reply (local) in %ss", elapsed)
    return jsonify({
        "reply": reply,
        "source": "local",
        "processing_time": elapsed,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)