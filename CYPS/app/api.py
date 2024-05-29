# app/api.py

from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)

@api_bp.route('/example', methods=['GET'])
def example():
    return jsonify({"message": "This is an example API endpoint."})

# More API endpoints as needed
