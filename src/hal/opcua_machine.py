# Import the OPC UA client library.
import json
import logging

from asyncua.sync import Client
from asyncua import ua

from time import sleep, time
#import serial

from .interface import HAL

_logger = logging.getLogger(__name__)

class Hahnenschwanz2(HAL):
    """Hardware Abstraction Layer for the Hahnenschwanz2 machine."""
    _client: Client = None
 #   cup_reader: serial.Serial = None
    _url = "opc.tcp://192.168.5.99:4840/"
    _prefix = "ns=4;s=|var|c300.Application.Com"

    def initialize(self):
        client = Client(url=self._url)
        client.connect()
        #if not client.connect():
        #    raise Exception("Could not connect to OPC UA server")
        self._client = client
        #self.cup_reader = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

        self._status_node = self._client.get_node(self._prefix+".statuscode")
        self._ingredient_node = self._client.get_node(self._prefix+".ingredient")
        self._scale_node = self._client.get_node(self._prefix+".scale")


    def dispense(self, position, amount):
        """Dispense a given amount at a position.
        Args:
            position (str): The position to dispense at.
            amount (float): The amount to dispense.
        """
        self._ingredient_node.write_value(ua.Variant(json.dumps({"position": position , "amount": amount }), ua.VariantType.String))
        start_time = time()
        while start_time + 30 > time():
            status = self._status_node.read_value()
            ingredient = self._ingredient_node.read_value()
            if  status == 101 or status == 100 and ingredient == "done":
                return
            sleep(0.1)
        raise Exception("Timeout while waiting for machine to finish dispensing ingredient")


    def home(self):
        """Move the machine to the extraction position."""
        self._ingredient_node.write_value(ua.Variant(json.dumps({"position": 0, "amount": 0 }), ua.VariantType.String))
        start_time = time()
        while start_time + 30 > time():
            status = self._status_node.read_value()
            ingredient = self._ingredient_node.read_value()
            if  status == 101 or status == 100 and ingredient == "done":
                return
            sleep(0.1)
        raise Exception("Timeout while waiting for machine to finish dispensing ingredient")

    def read_scale(self):
        """Read the scale and return the weight."""
        #TODO: subscibe pattern!
        _in = self.client.get_node("ns=4;s=|var|c300.Application.GVL.Scale")
        return _in.read_value()

    def read_cup(self):
        """Read the cup ID and return it."""
        return self.cup_reader.readline()

    def cleanup(self):
        """Perform any necessary cleanup or shutdown tasks."""
        self.home()
        self.client.disconnect()
        self.cup_reader.close()
