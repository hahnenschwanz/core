from flask import Blueprint, request, jsonify

from models.order import Order
from db import db
import datetime
from machine import machine, MachineError

order_bp = Blueprint("order", __name__)

@order_bp.route("/api/order", methods=["POST"])
def create_order():
    cocktail_id = request.get_json()
    #user_cup = db.get_user_cup(data.get("userId"))
    #
    #if user_cup is None:
    #    return "No cup found for the user", 400
    #
    #if db.get_order_by_cup(user_cup) is not None:
    #    return "A cocktail is already being prepared for this user", 409
    #order = Order(data.get("userId"), cocktail_id)
    #order.cup = user_cup
    #order.timestamp = datetime.datetime.now()
    #
    #db.order_create(order)
    cocktail = db.get_cocktail(cocktail_id)
    try:
        machine.mix(cocktail)
    except MachineError as e:
        return str(e), 400
    return jsonify("Cocktail is being prepared", 202)


abort_bp = Blueprint("abort", __name__)

@abort_bp.route("/api/abort", methods=["POST"])
def abort_order():
    try:
        machine.abort()
    except MachineError as e:
        return str(e), 400
    return jsonify("No Cocktail is being prepared", 409)
