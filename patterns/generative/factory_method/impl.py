from abc import ABC, abstractmethod

class Pastry(ABC):
    """Базовый класс для всех видов пирожных."""

    @abstractmethod
    def prepare(self):
        """Метод для подготовки пирожного."""
        pass

    @abstractmethod
    def bake(self):
        """Метод для выпекания пирожного."""
        pass

    @abstractmethod
    def box(self):
        """Метод для упаковки пирожного."""
        pass


class Croissant(Pastry):
    """Класс, представляющий круассан."""

    def prepare(self):
        return "Preparing croissant dough"

    def bake(self):
        return "Baking croissant at 200 degrees"

    def box(self):
        return "Packing croissant in a box"


class Muffin(Pastry):
    """Класс, представляющий маффин."""

    def prepare(self):
        return "Preparing muffin batter"

    def bake(self):
        return "Baking muffin at 180 degrees"

    def box(self):
        return "Packing muffin in a box"


class PastryFactory(ABC):
    """Абстрактный класс для фабрики пирожных."""

    @abstractmethod
    def create_pastry(self):
        """Фабричный метод для создания пирожного."""
        pass


class CroissantFactory(PastryFactory):
    """Конкретная фабрика для создания круассанов."""

    def create_pastry(self):
        return Croissant()


class MuffinFactory(PastryFactory):
    """Конкретная фабрика для создания маффинов."""

    def create_pastry(self):
        return Muffin()


def order_pastry(factory: PastryFactory):
    """Функция для заказа пирожного через фабрику.

    Args:
        factory (PastryFactory): Фабрика для создания пирожного.
    """
    pastry = factory.create_pastry()
    print(pastry.prepare())
    print(pastry.bake())
    print(pastry.box())


if __name__ == "__main__":
    print("Ordering a croissant:")
    order_pastry(CroissantFactory())

    print("\nOrdering a muffin:")
    order_pastry(MuffinFactory())
