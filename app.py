from flask import Flask, jsonify
from flask_cors import CORS
import os
import firebase_admin
from firebase_admin import credentials, firestore


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

cred = credentials.Certificate("firestore_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/swag')
def swag():
    """
    Returns a JSON response with the text "swag"
    """
    
    COLLECTION_NAME = "swag"
    PROJECT_ID = "wil2023-408410"
    try:
        docs = db.collection(COLLECTION_NAME).stream()
        swag_list = []
        for doc in docs:
            swag_item = {
                "name": doc.to_dict().get("name"),
                "description": doc.to_dict().get("description"),
            }
            swag_list.append(swag_item)
        return jsonify(swag_list)
    except Exception as e:
        return jsonify({"error": str(e)}),500
  

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
