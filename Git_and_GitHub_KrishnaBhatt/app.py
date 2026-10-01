from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
import os
import uuid
import hashlib

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB", "git_github_assignment")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
db = client[DB_NAME]
todo_collection = db["todos"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["GET"])
def api():
    return jsonify({
        "message": "Git & GitHub Flask API",
        "assignment": "DEVOPS",
        "status": "success"
    })

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json(silent=True) or request.form

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")
    item_id = data.get("itemId")
    item_uuid = data.get("itemUUID")
    item_hash = data.get("itemHash")

    if not item_name or not item_description:
        return jsonify({
            "success": False,
            "message": "itemName and itemDescription are required"
        }), 400

    item_uuid = item_uuid or str(uuid.uuid4())
    item_hash = item_hash or hashlib.sha256(
        f"{item_name}:{item_description}".encode()
    ).hexdigest()

    todo = {
        "itemName": item_name,
        "itemDescription": item_description,
        "itemId": item_id,
        "itemUUID": item_uuid,
        "itemHash": item_hash
    }

    try:
        result = todo_collection.insert_one(todo)
        return jsonify({
            "success": True,
            "message": "To-Do item saved successfully",
            "id": str(result.inserted_id),
            "item": todo
        }), 201
    except PyMongoError as exc:
        return jsonify({
            "success": False,
            "message": "Database error",
            "error": str(exc)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
