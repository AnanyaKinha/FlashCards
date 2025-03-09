from flask import Flask, request, jsonify, render_template
import json
import random

app = Flask(__name__, static_folder="static", template_folder="templates")

QUESTION_FILE = "questions.json"

def load_questions():
    try:
        with open(QUESTION_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_questions(questions):
    with open(QUESTION_FILE, "w") as f:
        json.dump(questions, f, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/topics", methods=["GET"])
def get_topics():
    questions = load_questions()
    return jsonify({"topics": list(questions.keys())})

@app.route("/question", methods=["GET"])
def get_question():
    topic = request.args.get("topic")
    questions = load_questions()
    if topic not in questions:
        return jsonify({"error": "Topic not found"}), 404
    question = random.choice(questions[topic])
    return jsonify({"question": question["q"]})

@app.route("/answer", methods=["POST"])
def get_answer():
    data = request.json
    topic = data.get("topic")
    question = data.get("question")
    questions = load_questions()
    if topic not in questions:
        return jsonify({"error": "Topic not found"}), 404
    for q in questions[topic]:
        if q["q"] == question:
            return jsonify({"answer": q["a"]})
    return jsonify({"error": "Question not found"}), 404

@app.route("/add", methods=["POST"])
def add_question():
    data = request.json
    topic = data.get("topic")
    question = data.get("question")
    answer = data.get("answer")
    if not topic or not question or not answer:
        return jsonify({"error": "Missing data"}), 400
    
    questions = load_questions()
    if topic not in questions:
        questions[topic] = []
    
    questions[topic].append({"q": question, "a": answer})
    save_questions(questions)
    return jsonify({"message": "Question added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
