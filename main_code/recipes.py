class Recipes:
    
    def __init__(self, ingredients: list, main_ingredient):
        self.ingredients = ingredients
        self.main_ingredient = main_ingredient

    def main_ingredient(self):
        return self.main_ingredient