from hal.opcua_machine import Hahnenschwanz2
import time

if __name__ == "__main__":
    hal = Hahnenschwanz2()
    hal.initialize()
    for i in range(1, 11):
        hal.dispense(i, 0.02)
    hal.home()