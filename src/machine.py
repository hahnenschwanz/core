from config import planner, hal
from api.events import event_order_change
from models.order import Order

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

    def mix(self, order: Order):
        if self.state == State.RUNNING:
            raise MachineError("Machine is already running")
        self.state = State.RUNNING
        self.active_order = order.id
        steps = planner.plan(order.cocktail)
        step_counter = 0
        for step in steps:
            if self.state == State.ABORT:
                break
            step_counter += 1
            hal.dispense(step.position, step.amount)
            event_order_change(order.id,  step_counter / len(steps)) #problem bei doppelten zutaten?
        hal.home()
        self.state = State.IDLE
        self.active_order = None
    
    def abort(self):
        if self.state == State.IDLE:
            raise MachineError("Machine is not running")
        self.state = State.ABORT
        hal.home()
        self.state = State.IDLE
        self.active_order = None

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