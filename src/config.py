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
        "Licor 43": 1,
        "Tonic Water": 11,
        "Tequila": 2,
        "Cranberrysaft": 12,
        "Batida de Coco": 3,
        "Orangensaft": 13,
        "Vodka": 4,
        "Ananassaft": 14,
        "Blue Curacao": 5,
        "Gin": 6,
        "Kirschsaft": 15,
        "Pfirsichlik": 7,
        "Maracuja": 16,
        "Bacardi": 8,
        "Bannanennektar": 17,
        "Granadinensyrup": 9,
        "Sahne": 18,
        "Zitronensaft": 10,
    }
}
from planner.interface import Planner
from planner.Hahnenschwanz2Planner import Hahnenschwanz2Planner
planner = Hahnenschwanz2Planner(machine_capabilities)