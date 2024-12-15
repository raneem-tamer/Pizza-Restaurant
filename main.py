from pizza.pizza import MargheritaPizza, PepperoniPizza
from pizza.toppings import CheeseTopping, OlivesTopping, MushroomsTopping
from inventory.inventory_manager import InventoryManager
from payment.payment_methods import PayPalPayment, CreditCardPayment
from payment.payment_context import PaymentContext


def main():
    inventory_manager = InventoryManager()
    print("Welcome to the Pizza Restaurant!")

    while True:
        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0. Exit")
        pizza_choice = input("Enter your choice: ")

        if pizza_choice == '0':
            break

        pizza = None
        if pizza_choice == '1' and inventory_manager.check_and_decrement("Margherita"):
            pizza = MargheritaPizza()
        elif pizza_choice == '2' and inventory_manager.check_and_decrement("Pepperoni"):
            pizza = PepperoniPizza()
        else:
            print("Pizza out of stock!")
            continue

        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter your choice: ")

            if topping_choice == '1' and inventory_manager.check_and_decrement("Cheese"):
                pizza = CheeseTopping(pizza)
            elif topping_choice == '2' and inventory_manager.check_and_decrement("Olives"):
                pizza = OlivesTopping(pizza)
            elif topping_choice == '3' and inventory_manager.check_and_decrement("Mushrooms"):
                pizza = MushroomsTopping(pizza)
            elif topping_choice == '4':
                break
            else:
                print("Topping unavailable or out of stock!")

        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        print("\nChoose a payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter your choice: ")

        payment_context = PaymentContext(PayPalPayment() if payment_choice == '1' else CreditCardPayment())
        payment_context.execute_payment(pizza.get_cost())

        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()
