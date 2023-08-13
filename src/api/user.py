from flask import Blueprint, jsonify, request
from models.user import User
from db import db

user_bp = Blueprint("user", __name__)

@user_bp.route("/api/user", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    user = User(name)
    db.user_create(user)
    return jsonify(user)

@user_bp.route("/api/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = db.get_user(user_id)
    if not user:
        return "User not found", 404
    return jsonify(user)

@user_bp.route("/api/user/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = User(user_id, data.get("name"), data.get("cups"))
    db.user_update(user)
    return jsonify(user)

@user_bp.route("/api/user/<user_id>/order", methods=["GET"])
def get_user_orders(user_id):
    user = users.get(user_id)
    if not user:
        return "User not found", 404

    user_orders = [order for order in orders if order.user_id == user_id]
    return jsonify([order.__dict__ for order in user_orders])

