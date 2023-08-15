CUPS_ENABLED = True
OPC_SERVER = "opc.tcp://localhost:4840"
OPC_NAMESPACE = "http://opcfoundation.org/UA/"

BASE_URL = "http://localhost:3000"

DATABASE_FILE = "database.db"

from hal.interface import HAL
from hal.opcua_machine import Hahnenschwanz2
from hal.mock import MockHal
#hal = Hahnenschwanz2()
hal = MockHal()
try:
    hal.initialize()
except:
    pass


machine_capabilities = {
    "dispenser": {
        "Vodka": 1,
        "Peach Schnapps": 4,
        "Orange Juice": 12,
        "Cranberry Juice": 14,
        "Grapefruit Juice": 16,
        "Lemon Juice": 18,
        "Lime": 20,
        "Pineapple Juice": 22,
        "Grenadine": 24,
        "Simple Syrup": 26,
        "Sugar": 28,
        "White rum": 30,
        "Mint": 30,
    }
}
from planner.interface import Planner
from planner.Hahnenschwanz2Planner import Hahnenschwanz2Planner
planner = Hahnenschwanz2Planner(machine_capabilities)