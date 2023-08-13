'''
POST /admin/scale/tare
  Setzt die Waage auf Null

POST /admin/scale/scaling
  Setzt den Scaling-Multiplier der Wage
  Request: number

POST /admin/clean/start
  Startet den Reinigungsmodus

POST /admin/clean/Stop
  Stoppt den Reinigungsmodus
'''

from flask import Blueprint, jsonify
from db import db

admin = Blueprint("admin", __name__)

@admin.route("/admin/scale/tare", methods=["POST"])
def tare():
    return jsonify("Not Implemented"), 500

@admin.route("/admin/scale/scaling", methods=["POST"])
def scaling():
    return jsonify("Not Implemented"), 500

@admin.route("/admin/clean/start", methods=["POST"])
def clean_start():
    return jsonify("Not Implemented"), 500

@admin.route("/admin/clean/stop", methods=["POST"])
def clean_stop():
    return jsonify("Not Implemented"), 500

@admin.route("/admin/clean/status", methods=["GET"])
def clean_status():
    return jsonify("Not Implemented"), 500