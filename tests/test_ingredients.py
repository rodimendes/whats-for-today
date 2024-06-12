from main_code.recipes import Recipes

test_recipe = Recipes(ingredients=['arroz', 'maionese', 'batata', 'frango'], main_ingredient='frango')

def test_listOfIngredients():
    """
    Test to check if the user is passing a list of ingredients.
    """
    assert len(test_recipe.ingredients) != 0


def test_checkRecipesWithEspecifiedIngredients():
    """
    Check recipes with ingredients passed by the user. The results must be shown sorted.
    """
    assert sorted(test_recipe.ingredients) == ['arroz', 'batata', 'frango', 'maionese']


def test_checkPresenceOfAllergicIngredientes():
    """
    The function must return True or False based on presence allergenic ingredients.
    """
    pass

