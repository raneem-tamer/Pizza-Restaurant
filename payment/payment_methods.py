from abc import ABC, abstractmethod

# Base Payment Method
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


# PayPal Payment
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount:.2f} via PayPal...")


# Credit Card Payment
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Processing payment of ${amount:.2f} via Credit Card...")
