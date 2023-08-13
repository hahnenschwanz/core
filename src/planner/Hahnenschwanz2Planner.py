from .interface import Planner, Step

class Hahnenschwanz2Planner(Planner):
    def plan(self, cocktail, machine_capabilities):
        """Plan the mixing sequence based on machine capabilities.

        Args:
            machine_capabilities (dict): A dictionary describing the capabilities of the machine.

        Returns:
            list: A list of steps representing the mixing sequence.
        """
        steps = []
        for ingredient in cocktail.ingredients:
            pos = machine_capabilities.ingredients[ingredient] 
            steps.append(Step(pos, ingredient.amount))
        return steps