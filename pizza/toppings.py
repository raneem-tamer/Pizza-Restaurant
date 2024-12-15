from pizza.pizza import Pizza

# Topping Decorator
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_description(self):
        return self._pizza.get_description()

    def get_cost(self):
        return self._pizza.get_cost()


# Cheese Topping
class CheeseTopping(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Cheese"

    def get_cost(self):
        return self._pizza.get_cost() + 1.0


# Olives Topping
class OlivesTopping(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Olives"

    def get_cost(self):
        return self._pizza.get_cost() + 0.5


# Mushrooms Topping
class MushroomsTopping(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Mushrooms"

    def get_cost(self):
        return self._pizza.get_cost() + 0.7
