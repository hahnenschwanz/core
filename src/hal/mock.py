from .hal import HAL
import logging
_logger = logging.getLogger(__name__)

class MockHal(HAL):
    

    def initialize(self):
        __logger.info("Initializing Mock HAL")


    def dispense(self, position, amount):
        __logger.info("Mock HAL: Dispensing %s ml from position %s", amount, position)

    def home(self):
        __logger.info("Mock HAL: Homing")

    def read_scale(self):
        """Read the scale and return the weight."""
        return 300

    def read_cup(self):
        """Read the cup ID and return it."""
        return 0

    def cleanup(self):
        """Perform any necessary cleanup or shutdown tasks."""
        self.home()


