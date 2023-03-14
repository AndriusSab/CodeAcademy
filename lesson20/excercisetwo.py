# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
# Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.

class Smoothie:
    def __init__(self, ingredients: dict) -> None:
        self.ingredients = ingredients
          

    def get_cost(self) -> float:
        total_cost = 0
        
        for ingredient, price in self.ingredients.items():
            total_cost += price
        return total_cost

    def get_price(self) -> None:
        K = 1.5   # coeficient
        cost = self.get_cost()
        price = cost + cost * K
        print(round(price, 2))

class TropicalSmoothie(Smoothie):

    def get_name(self) -> None:
        sorted_ingredients = sorted(self.ingredients.keys())
        print(f"Your smoothe contains these ingredients: {sorted_ingredients}")
       

class TropicalSmoothie(Smoothie):

Tropic_smoothie_ingredients = {"strawberies":5,
    "bannana":1,
    "orange_juice":2,
    "pineapple":2,
    "ice":0.5,
    "honey":1
    }

class EasySmoothie(Smoothie):

Tropic_smoothie_ingredients = {"strawberies":5,
    "bannana":1,
    "orange_juice":2,
    "pineapple":2,
    "ice":0.5,
    "honey":1
    }

a = Smoothie(Tropic_smoothie_ingredients)
print(a.get_cost())
a.get_price()
a.get_name()