from .interface import Planner, Step

class Hahnenschwanz2Planner(Planner):
    def __init__(self, machine_capabilities):
        self._machine_capabilities = machine_capabilities

    def plan(self, cocktail):
        """Plan the mixing sequence based on machine capabilities.

        Args:
            machine_capabilities (dict): A dictionary describing the capabilities of the machine.

        Returns:
            list: A list of steps representing the mixing sequence.
        """
        steps = []
        for ingredient, amount in cocktail.recipe:
            pos = self._machine_capabilities["dispenser"][ingredient.name] 
            steps.append(Step(pos, amount))
        return steps