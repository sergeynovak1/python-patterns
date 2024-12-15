class Component:
    """Базовый класс для всех компонентов в паттерне Composite."""

    def operation(self):
        """Определяет общий интерфейс для всех элементов."""
        pass


class Leaf(Component):
    """Класс 'Лист', который представляет собой конечный элемент в структуре."""

    def __init__(self, name):
        """Инициализация нового листа.

        Args:
            name (str): имя листа.
        """
        self.name = name

    def operation(self):
        """Возвращает имя листа."""
        return self.name


class Composite(Component):
    """Класс 'Композит', который может содержать другие компоненты (листы или композиты)."""

    def __init__(self):
        """Инициализация нового композита."""
        self.children = []

    def add(self, component):
        """Добавляет компонент (лист или композит) в структуру.

        Args:
            component (Component): компонент, который будет добавлен.
        """
        self.children.append(component)

    def remove(self, component):
        """Удаляет компонент из структуры.

        Args:
            component (Component): компонент, который будет удален.
        """
        self.children.remove(component)

    def operation(self):
        """Выполняет операцию над всеми дочерними компонентами и возвращает их результаты."""
        result = []
        for child in self.children:
            result.append(child.operation())
        return result


if __name__ == "__main__":
    leaf1 = Leaf("Лист 1")
    leaf2 = Leaf("Лист 2")

    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)

    print(composite.operation())  # Вывод: ['Лист 1', 'Лист 2']
