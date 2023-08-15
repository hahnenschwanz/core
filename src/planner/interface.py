
from abc import ABC, abstractmethod

class Step(object):
    def __init__(self, position, amount):
        self.position = position
        self.amount = amount

    def __repr__(self):
        return f"Step({self.position}, {self.amount})"

    def __str__(self):
        self.__repr__()

    def serialize(self):
        return {
            "position": self.position,
            "amount": self.amount
        }

class Planner(ABC):
    @abstractmethod
    def plan(self, cocktail, machine_capabilities):
        """Plan the mixing sequence based on machine capabilities.

        Args:
            machine_capabilities (dict): A dictionary describing the capabilities of the machine.

        Returns:
            list: A list of steps representing the mixing sequence.
        """
        pass