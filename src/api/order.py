from flask import Blueprint, request, jsonify

from models.order import Order
from db import db
import datetime
from machine import machine, MachineError

order_bp = Blueprint("order", __name__)

@order_bp.route("/api/order", methods=["POST"])
def create_order():
    data = request.get_json()
    cocktail_id = data.get("CocktailId")
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
    #db.session.add(Order(data.get("userId"), cocktail_id))

    try:
        machine.mix(cocktail_id)
    except MachineError as e:
        return str(e), 400
    return jsonify("Cocktail is being prepared", 202)