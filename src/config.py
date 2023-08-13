CUPS_ENABLED = True
OPC_SERVER = "opc.tcp://localhost:4840"
OPC_NAMESPACE = "http://opcfoundation.org/UA/"

BASE_URL = "http://localhost:3000"

DATABASE_FILE = "database.db"

from hal.interface import HAL
from hal.opcua_machine import Hahnenschwanz2
hal = Hahnenschwanz2()
hal.initialize()


machine_capabilities = {
    "dispenser": {
        "Vodka": 1,
        "Peach Schnapps": 4,
        "Orange Juice": 12,
        "Cranberry Juice": 14,
    }
}
from planner.interface import Planner
from planner.Hahnenschwanz2Planner import Hahnenschwanz2Planner
planner = Hahnenschwanz2Planner(machine_capabilities)