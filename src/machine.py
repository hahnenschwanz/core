from config import planner, hal
from api.events import event_order_change
from models.order import Order
from models.cocktail import Cocktail

class State:
    IDLE = 0
    RUNNING = 1
    ABORT = 2
    ERROR = 3

class MachineError(Exception):
    pass    


class Machine:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Machine, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.state = State.IDLE
        self.active_order = None
        self.active_cup = None
        self.active_user = None

    def mix(self, cocktail: Cocktail):
        if self.state != State.IDLE:
            raise MachineError("Machine is not idle")
        self.state = State.RUNNING
        event_order_change(cocktail.id, 0)
        #self.active_order = order.id
        steps = planner.plan(cocktail)
        step_counter = 0
        for step in steps:
            if self.state != State.RUNNING:
                break
            step_counter += 1
            event_order_change(cocktail.id, step_counter / len(steps) * 100)
            hal.dispense(step.position, step.amount)
        hal.home()
        if self.state != State.ERROR:
            self.state = State.IDLE
        self.active_order = None
        event_order_change(None, None)
    
    def abort(self):
        if self.state == State.IDLE:
            raise MachineError("Machine is not running")
        self.state = State.ABORT
        hal.home()
        self.state = State.IDLE
        self.active_order = None
        event_order_change(None, None)

    def stop(self):
        if self.state == State.IDLE:
            raise MachineError("Machine is not running")
        self.state = State.ERROR
        self.active_order = None

    def unlock(self):
        if self.state != State.ERROR:
            raise MachineError("Machine is not in error state")
        self.state = State.IDLE
    
machine = Machine()
