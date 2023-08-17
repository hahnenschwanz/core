import json
import time

from flask_sock import Sock
from db import db

sock = Sock()

cup_state = {"type": "CupChange", "body": {"cup": None, "user": None}}
order_state = {"type": "OrderChange", "body": {"cocktail": None, "progress": None, "notice": None}}

@sock.route('/api/events')
def ws_socket(ws):
    while True:
        ws.send(json.dumps(cup_state))
        ws.send(json.dumps(order_state))
        time.sleep(1)

def event_cup_change(cup_id):
    global cup_state
    #for user in db.get_users():
        #find cup_id 
    #    for cup in user.cups:
    #        if cup == cup_id:
    #            user_id = user.id
    #            break
    #if user_id is None:
    #    cup_id = None
    user_id = None
    cup_state = {"type": "CupChange", "body": {"cup": cup_id, "user": user_id}}

def event_order_change(cocktail_id: str, progress: float, notice: str = None):
    global order_state

    event_body = {"cocktail": cocktail_id, "progress": progress, "notice": notice}
    order_state = {"type": "OrderChange", "body": event_body}


#@ws.on("connect", namespace="/events")
#def handle_connect():
#    # Get initial cup and order status and send it to the client on connection
#    emit_cup_change_event()
#    emit_order_change_event()

#def emit_cup_change_event(cup_id):
#    # Emit a CupChangeEvent with the current cup and user data
#    user_id = None
#    for user in users:
#        #find cup_id 
#        if cup_id in user.cups:
#            user_id = user.id
#            break
#    ws.emit("event", {"type": "CupChange", "body": {"cup": cup_id, "user": user_id}}, json=True, namespace="/events")
#    return
    
#def emit_order_change_event():
#    # Emit an OrderChangeEvent with the current order and progress data
#    active_order = None
#    for order in orders:
#        if order.cup:
#            active_order = {"order": order.__dict__, "progress": None}
#            break
#    ws.emit("event", {"type": "OrderChange", "body": active_order}, json=True, namespace="/events")
#    return
