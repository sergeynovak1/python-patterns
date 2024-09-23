class Borg:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls)
        obj.__dict__ = cls._shared_state
        return obj

class MyClass(Borg):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    a = MyClass("Первый экземпляр")
    b = MyClass("Второй экземпляр")

    print("Состояние экземпляров до изменений:")
    print(f"a.name: {a.name}")  # Вывод: "Первый экземпляр"
    print(f"b.name: {b.name}")  # Вывод: "Второй экземпляр"

    # Изменяем состояние одного экземпляра
    a.name = "Измененный экземпляр"

    print("\nСостояние экземпляров после изменений:")
    print(f"a.name: {a.name}")  # Вывод: "Измененный экземпляр"
    print(f"b.name: {b.name}")  # Вывод: "Измененный экземпляр"

    print(f"a is b: {a is b}")  # Вывод: False


