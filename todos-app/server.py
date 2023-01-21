import os
from flask import Flask, request
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.uri_parser import parse_uri
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

app = Flask(__name__)

# load environment variables from .env file
load_dotenv()

# Get the MongoDB URI from the environment variable
mongodb_uri = os.environ.get("MONGODB_URL")

# Parse the URI to extract the credentials
mongodb_credentials = parse_uri(mongodb_uri)

# Connect to the MongoDB database
client = MongoClient(mongodb_uri)
db = client[mongodb_credentials['database']]

@app.route('/todo', methods=['GET'])
def get_all_todos():
    todos = list(db.todos.find())
    return json.loads(dumps(todos))

@app.route('/todo/<id>', methods=['GET'])
def get_todo(id):
    todo = db.todos.find_one({'_id': ObjectId(id)})
    return json.loads(dumps(todo))

@app.route('/todo', methods=['POST'])
def add_todo():
    todo = request.json
    db.todos.insert_one(todo)
    return {'status': 'success'}

@app.route('/todo/<id>', methods=['PUT'])
def update_todo(id):
    todo = request.json
    db.todos.update_one({'_id': ObjectId(id)}, {'$set': todo})
    return {'status': 'success'}

@app.route('/todo/<id>', methods=['PATCH'])
def patch_todo(id):
    todo = request.json
    db.todos.update_one({'_id': ObjectId(id)}, {'$set': todo})
    return {'status': 'success'}

@app.route('/todo/<id>', methods=['DELETE'])
def delete_todo(id):
    db.todos.delete_one({'_id': ObjectId(id)})
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True)



