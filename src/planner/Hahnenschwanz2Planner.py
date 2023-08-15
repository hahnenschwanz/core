from .interface import Planner, Step
from db import db, Cocktail, CocktailIngredient, Ingredient

class Hahnenschwanz2Planner(Planner):
    def __init__(self, machine_capabilities):
        self._machine_capabilities = machine_capabilities

    def plan(self, cocktail_id):
        """Plan the mixing sequence based on machine capabilities.

        Args:
            machine_capabilities (dict): A dictionary describing the capabilities of the machine.

        Returns:
            list: A list of steps representing the mixing sequence.
        """
        steps = []
        cocktail = db.session.execute(db.select(Cocktail).where(Cocktail.id == cocktail_id)).scalar()
        for cocktail_ingredient in cocktail.ingredients:
            pos = self._machine_capabilities["dispenser"][cocktail_ingredient.ingredient.name] 
            steps.append(Step(pos, cocktail_ingredient.amount))
        return steps