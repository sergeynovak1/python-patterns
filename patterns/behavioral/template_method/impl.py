from abc import ABC, abstractmethod

# Абстрактный класс
class Beverage(ABC):
    """Абстрактный класс, представляющий напиток."""

    def prepare_recipe(self):
        """Шаблонный метод, определяющий алгоритм приготовления напитка."""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        """Общий шаг для всех напитков: кипячение воды."""
        print("Boiling water")

    def pour_in_cup(self):
        """Общий шаг для всех напитков: наливание напитка в чашку."""
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        """Абстрактный метод для заваривания напитка."""
        pass

    @abstractmethod
    def add_condiments(self):
        """Абстрактный метод для добавления дополнительных ингредиентов."""
        pass


# Конкретные классы
class Tea(Beverage):
    """Класс, представляющий чай."""

    def brew(self):
        """Заваривание чая."""
        print("Steeping the tea")

    def add_condiments(self):
        """Добавление лимона в чай."""
        print("Adding lemon")


class Coffee(Beverage):
    """Класс, представляющий кофе."""

    def brew(self):
        """Заваривание кофе."""
        print("Dripping coffee through filter")

    def add_condiments(self):
        """Добавление сахара и молока в кофе."""
        print("Adding sugar and milk")


# Клиентский код
if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()

    print("Making tea:")
    tea.prepare_recipe()
    # Вывод:
    # Boiling water
    # Steeping the tea
    # Pouring into cup
    # Adding lemon

    print("\nMaking coffee:")
    coffee.prepare_recipe()
    # Вывод:
    # Boiling water
    # Dripping coffee through filter
    # Pouring into cup
    # Adding sugar and milk
