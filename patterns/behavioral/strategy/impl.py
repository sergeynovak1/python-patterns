class PaymentStrategy:
    """Базовый класс для всех стратегий оплаты."""

    def pay(self, amount):
        """Определяет общий интерфейс для всех стратегий оплаты.

        Args:
            amount (float): сумма для оплаты.
        """
        pass


class CreditCardPayment(PaymentStrategy):
    """Стратегия оплаты кредитной картой."""

    def pay(self, amount):
        """Оплата с использованием кредитной карты.

        Args:
            amount (float): сумма для оплаты.
        """
        print(f"Paying {amount} using Credit Card")


class PayPalPayment(PaymentStrategy):
    """Стратегия оплаты через PayPal."""

    def pay(self, amount):
        """Оплата с использованием PayPal.

        Args:
            amount (float): сумма для оплаты.
        """
        print(f"Paying {amount} using PayPal")


class ShoppingCart:
    """Корзина для покупок, которая использует стратегии оплаты."""

    def __init__(self):
        """Инициализация новой корзины для покупок."""
        self.items = []
        self.payment_strategy = None

    def set_payment_strategy(self, strategy: PaymentStrategy):
        """Устанавливает стратегию оплаты.

        Args:
            strategy (PaymentStrategy): стратегия оплаты.
        """
        self.payment_strategy = strategy

    def checkout(self, amount):
        """Осуществляет оплату с использованием установленной стратегии.

        Args:
            amount (float): сумма для оплаты.
        """
        if self.payment_strategy is not None:
            self.payment_strategy.pay(amount)
        else:
            print("Payment strategy not set.")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.set_payment_strategy(CreditCardPayment())
    cart.checkout(100)

    cart.set_payment_strategy(PayPalPayment())
    cart.checkout(200)
