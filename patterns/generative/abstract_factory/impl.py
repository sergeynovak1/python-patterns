from abc import ABC, abstractmethod


class Chair(ABC):
    """Базовый интерфейс для стульев."""

    @abstractmethod
    def sit_on(self):
        pass


class Table(ABC):
    """Базовый интерфейс для столов."""

    @abstractmethod
    def dine_on(self):
        pass


class ModernChair(Chair):
    """Конкретный класс для современного стула."""

    def sit_on(self):
        return "Sitting on a modern chair"


class VictorianChair(Chair):
    """Конкретный класс для викторианского стула."""

    def sit_on(self):
        return "Sitting on a Victorian chair"


class ModernTable(Table):
    """Конкретный класс для современного стола."""

    def dine_on(self):
        return "Dining on a modern table"


class VictorianTable(Table):
    """Конкретный класс для викторианского стола."""

    def dine_on(self):
        return "Dining on a Victorian table"


class FurnitureFactory(ABC):
    """Абстрактная фабрика для создания мебели."""

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


class ModernFurnitureFactory(FurnitureFactory):
    """Конкретная фабрика для создания современной мебели."""

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()


class VictorianFurnitureFactory(FurnitureFactory):
    """Конкретная фабрика для создания викторианской мебели."""

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()


def client_code(factory: FurnitureFactory):
    """Функция клиентского кода, использующая фабрику для создания продуктов.

    Args:
        factory (FurnitureFactory): Фабрика для создания мебели.
    """
    chair = factory.create_chair()
    table = factory.create_table()

    print(chair.sit_on())
    print(table.dine_on())


if __name__ == "__main__":
    print("Client: Testing client code with the ModernFurnitureFactory:")
    client_code(ModernFurnitureFactory())

    print("\nClient: Testing the same client code with the VictorianFurnitureFactory:")
    client_code(VictorianFurnitureFactory())
