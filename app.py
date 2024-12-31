from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/hello')
def hello():
    """
    Returns a JSON response with the text "Hello World"
    """
    return jsonify({'text': 'Hello World'})

@app.route('/wassup')
def wassup():
    """
    Returns a JSON response with the text "Wassup"
    """
    return jsonify({'text': 'Wassup'})

if __name__ == '__main__':
    app.run(debug=True)
