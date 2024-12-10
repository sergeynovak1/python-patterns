class Coffee:
    """Базовый класс для кофе."""

    def cost(self):
        """Возвращает стоимость кофе."""
        return 5

    def description(self):
        """Возвращает описание кофе."""
        return "Coffee"


class CoffeeDecorator(Coffee):
    """Абстрактный класс декоратора для кофе."""

    def __init__(self, coffee):
        """Инициализация декоратора с кофе.

        Args:
            coffee (Coffee): кофе, который будет декорирован.
        """
        self._coffee = coffee

    def cost(self):
        """Возвращает стоимость декорированного кофе."""
        return self._coffee.cost()

    def description(self):
        """Возвращает описание декорированного кофе."""
        return self._coffee.description()


class MilkDecorator(CoffeeDecorator):
    """Конкретный декоратор, который добавляет молоко к кофе."""

    def cost(self):
        """Возвращает стоимость кофе с молоком."""
        return self._coffee.cost() + 1

    def description(self):
        """Возвращает описание кофе с молоком."""
        return f"{self._coffee.description()} + Milk"


class SugarDecorator(CoffeeDecorator):
    """Конкретный декоратор, который добавляет сахар к кофе."""

    def cost(self):
        """Возвращает стоимость кофе с сахаром."""
        return self._coffee.cost() + 0.5

    def description(self):
        """Возвращает описание кофе с сахаром."""
        return f"{self._coffee.description()} + Sugar"


class SyrupDecorator(CoffeeDecorator):
    """Конкретный декоратор, который добавляет сироп к кофе."""

    def cost(self):
        """Возвращает стоимость кофе с сиропом."""
        return self._coffee.cost() + 1.5

    def description(self):
        """Возвращает описание кофе с сиропом."""
        return f"{self._coffee.description()} + Syrup"


if __name__ == "__main__":
    # Заказываем обычный кофе
    coffee = Coffee()
    print(f"Description: {coffee.description()}, Cost: {coffee.cost()}")

    # Добавляем молоко
    milk_coffee = MilkDecorator(coffee)
    print(f"Description: {milk_coffee.description()}, Cost: {milk_coffee.cost()}")

    # Добавляем сахар
    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print(f"Description: {sugar_milk_coffee.description()}, Cost: {sugar_milk_coffee.cost()}")

    # Добавляем сироп
    syrup_sugar_milk_coffee = SyrupDecorator(sugar_milk_coffee)
    print(f"Description: {syrup_sugar_milk_coffee.description()}, Cost: {syrup_sugar_milk_coffee.cost()}")
