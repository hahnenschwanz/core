from abc import ABC, abstractmethod

class HAL(ABC):
    @abstractmethod
    def initialize(self):
        """Initialize the hardware interface."""
        pass

    #@abstractmethod
    #def set_cup(self, cup_id):
        """Set the cup with the given ID on the machine.

        Args:
            cup_id (str): The ID of the cup to set.
        """
    #    pass

    @abstractmethod
    def dispense(self, position, amount):
        """Dispense a given amount at a position.
        Args:
            position (str): The position to dispense at.
            amount (float): The amount to dispense.
        """
        pass

    @abstractmethod
    def home(self):
        """Move the machine to the extraction position."""
        pass

    @abstractmethod
    def read_scale(self):
        """Read the scale and return the weight."""
        pass

    @abstractmethod
    def read_cup(self):
        """Read the cup ID and return it."""
        pass

    @abstractmethod
    def cleanup(self):
        """Perform any necessary cleanup or shutdown tasks."""
        pass
