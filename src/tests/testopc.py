import sys


from asyncua.sync import Client
from asyncua import ua

if __name__ == "__main__":

    with Client("opc.tcp://192.168.5.99:4840/") as client:
        #print("Children of root are: ", client.nodes.root.get_children())

        # get a specific node knowing its node id
        #var = client.get_node(ua.NodeId(1002, 2))
        #var = client.get_node("ns=3;i=2002")
        #print(var)
        #var.read_data_value() # get value of node as a DataValue object
        #var.read_value() # get value of node as a python builtin
        #var.write_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.write_value(3.9) # set node value using implicit data type

        # Now getting a variable node using its browse path
        var = client.get_node("ns=4;s=|var|c300.Application.Com.statuscode")
        value = var.read_value()
        print("Value: ", value)
        #value = value +1 
        #var.write_value(ua.Variant(value, ua.VariantType.Int16))
        plc_prg = client.get_node("ns=4;s=|var|c300.Application.PLC_PRG.Methode2").get_parent()
        method = client.get_node("ns=4;s=|var|c300.Application.PLC_PRG.Methode2")
        method2 = client.get_node("ns=4;s=|var|c300.Application.PLC_PRG.Methode3")
        res = plc_prg.call_method(method2)
        #res = plc_prg.call_method(method, ua.Variant(3, ua.VariantType.Int16))
        #print("method result is: ", res)
        # Stacked myvar access
        # print("myvar is: ", root.get_children()[0].get_children()[1].get_variables()[0].read_value())

class HelloClient:
    def __init__(self, endpoint):
        self.client = Client(endpoint)

    def __enter__(self):
        self.client.connect()
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()
