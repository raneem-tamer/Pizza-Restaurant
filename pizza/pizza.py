from abc import ABC, abstractmethod

# Base Pizza Class
class Pizza(ABC):
    def __init__(self):
        self.description = "Base Pizza"
        self.cost = 0.0

    @abstractmethod
    def get_description(self):
        return self.description

    @abstractmethod
    def get_cost(self):
        return self.cost


# Margherita Pizza
class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 5.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Pepperoni Pizza
class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pepperoni Pizza"
        self.cost = 6.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
