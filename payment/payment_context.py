from payment.payment_methods import PaymentMethod

class PaymentContext:
    def __init__(self, payment_method: PaymentMethod):
        self._payment_method = payment_method

    def execute_payment(self, amount: float):
        self._payment_method.process_payment(amount)
