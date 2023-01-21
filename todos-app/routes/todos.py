from flask import Blueprint, jsonify, request
from flask_mongoengine import MongoEngine
from models.todo import Todo

todo_routes = Blueprint('todo_routes', __name__)

# Get all todos
@todo_routes.route('/', methods=['GET'])
def get_todos():
    todos = Todo.objects.all()
    return jsonify(todos.to_json())


# Get a single todo
@todo_routes.route('/<id>', methods=['GET'])
def get_todo(id):
    todo = Todo.objects.get(id=id)
    return jsonify(todo)

# Create a new todo
@todo_routes.route('/', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = Todo(**data)
    todo.save()
    return jsonify(todo), 201

# Update a todo
@todo_routes.route('/<id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    Todo.objects(id=id).update(**data)
    todo = Todo.objects.get(id=id)
    return jsonify(todo)

# Delete a todo
@todo_routes.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return jsonify(todo)
