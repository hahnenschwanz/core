from flask import Blueprint, request, jsonify

from db import db
import datetime
from machine import machine, MachineError

order_bp = Blueprint("order", __name__)

@order_bp.route("/api/order", methods=["POST"])
def create_order():
    data = request.get_json()
    cocktail_id = data.get("CocktailId")
    try:
        machine.mix(cocktail_id)
    except MachineError as e:
        return str(e), 400
    return jsonify("Cocktail is being prepared", 202)