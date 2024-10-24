from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


# Load questions from a JSON file
def load_questions():
    with open('questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

QUESTIONS = load_questions()

@app.route('/')
def home():
    return "Home"

# Route om het antwoord te ontvangen
@app.route('/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()  # Ontvang de JSON-gegevens van het verzoek
    correct = data.get('correct')  # Haal de string 'message' op

    # Verwerk de string (hier sturen we gewoon een bericht terug)
    response_message = f"De server ontving: test"

    return response_message  # Stuur een string terug naar de client
        

    

@app.route('/get-questions/<int:category_id>', methods=['GET'])
def get_questions_by_category(category_id):
    questions = QUESTIONS.get(str(category_id))
    
    if questions is None:
        return jsonify({"error": "Category not found"}), 404

    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)