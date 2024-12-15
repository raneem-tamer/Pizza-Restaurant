# Design Patterns Used in the Pizza Restaurant System

## **1. Decorator Pattern**

### **Purpose**
- Adds dynamic behavior to an object at runtime without altering its structure.

### **Implementation**
- `ToppingDecorator` dynamically adds `Cheese`, `Olives`, or `Mushrooms` to the base pizza.
- Allows creating combinations like `Margherita with Cheese and Mushrooms`.

### **Before Decorator Pattern**
Before applying the Decorator Pattern, the pizza creation was straightforward, with predefined combinations. Adding toppings required modifying the base `Pizza` class directly.

### **After Decorator Pattern**
With the Decorator Pattern, toppings are separate classes (`CheeseTopping`, `OlivesTopping`, `MushroomsTopping`). This allows dynamic addition of toppings to any pizza type without altering the base class.

### **Code Example**  

class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, {self._description}"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + self._cost

class CheeseTopping(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self._description = "Cheese"
        self._cost = 1.0

# Usage
margherita_pizza = MargheritaPizza()
cheese_margherita = CheeseTopping(margherita_pizza)
print(cheese_margherita.get_description())  # Margherita, Cheese
print(cheese_margherita.get_cost())  # 6.0


# Design Patterns in the Pizza Restaurant System

## **2. Singleton Pattern**

### **Purpose**
- Ensures only one instance of a class exists, providing a global point of access.

### **Implementation**
- `InventoryManager` is implemented as a singleton to ensure centralized inventory tracking.

### **Before Singleton Pattern**
Previously, inventory management was handled by creating multiple instances, leading to potential inconsistencies and duplication.

### **After Singleton Pattern**
Now, `InventoryManager` is a singleton, ensuring that all parts of the system share a single, consistent inventory instance.

### **Code Example**  

class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)
            cls._inventory = {
                "Margherita": 10,
                "Pepperoni": 10,
                "Cheese": 15,
                "Olives": 10,
                "Mushrooms": 12,
            }
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

# Usage
inventory_manager = InventoryManager()

### ** 3 Strategy Pattern**

## **Purpose**
- Allows selecting an algorithm (payment method) at runtime.

## **Implementation**
- `PaymentContext` dynamically processes payments using `PayPalPayment` or `CreditCardPayment`.

## **Before Strategy Pattern**
Payments were tightly coupled to specific payment methods within the system, making it difficult to add new methods.

## **After Strategy Pattern**
With the Strategy Pattern, new payment methods can be added by creating new subclasses of `PaymentMethod`, reducing code duplication and improving flexibility.

## **Code Example**  

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing payment of ${amount} via PayPal."

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing payment of ${amount} via Credit Card."

class PaymentContext:
    def __init__(self, payment_method: PaymentMethod):
        self._payment_method = payment_method

    def execute_payment(self, amount: float) -> str:
        return self._payment_method.process_payment(amount)

# Usage
payment_context = PaymentContext(PayPalPayment())
print(payment_context.execute_payment(7.20))


# Over Engineering

## **Definition**
Over Engineering occurs when too much complexity is added to a solution that could otherwise be simplified.

## **Example of Over Engineering**
Before applying design patterns, the Pizza restaurant system used a monolithic approach where multiple classes were tightly coupled. For example, integrating payment processing with inventory management required deep dependency management and redundant checks.

## **Code Example**  

class Pizza:
    def __init__(self, base: str, toppings: list):
        self.base = base
        self.toppings = toppings

    def get_description(self) -> str:
        return f"{self.base}, {', '.join(self.toppings)}"

    def get_cost(self) -> float:
        return 5.0 + sum(topping.cost for topping in self.toppings)

# Redundant complexity
class PaymentProcessor:
    def process_payment(self, payment_type: str, amount: float) -> bool:
        if payment_type == "credit_card":
            return self.process_credit_card(amount)
        elif payment_type == "paypal":
            return self.process_paypal(amount)
        return False

    def process_credit_card(self, amount: float) -> bool:
        # processing credit card logic
        pass

    def process_paypal(self, amount: float) -> bool:
        # processing PayPal logic
        pass

In the over-engineered system, the payment logic was tightly coupled to the payment type, leading to unnecessary complexity. With the Strategy Pattern, this complexity was replaced with a cleaner approach where payment methods are decoupled, and new methods can be easily added.