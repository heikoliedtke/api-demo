from flask import Flask, jsonify
from flask_cors import CORS
import os
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import firestore




app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

PROJECT_ID= "wil2023-408410"
COLLECTION_NAME= "swag"


key_path = './firestore_key.json'

if os.path.exists(key_path):
    db = firestore.Client.from_service_account_json(key_path)
    # ... proceed with Firestore operations ...
else:
    print(f"Error: The file '{key_path}' does not exist.")
    # ... handle the error appropriately (e.g., exit, raise an exception) ...


@app.route('/swag')
def swag():
    """
    Returns a JSON response with"
    """
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
