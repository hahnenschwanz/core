from flask import Blueprint, jsonify
from db import db

cocktail_bp = Blueprint("cocktail", __name__)

@cocktail_bp.route("/api/cocktail", methods=["GET"])
def get_cocktails():
    cocktails = db.get_cocktails()
    return jsonify([c.serialize() for c in cocktails])