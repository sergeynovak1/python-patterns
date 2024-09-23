class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'initialized'):  # Проверка на инициализацию
            self.value = value
            self.initialized = True


if __name__ == "__main__":
    singleton1 = Singleton("Первый экземпляр")
    singleton2 = Singleton("Второй экземпляр")

    print("Состояние экземпляров:")
    print(f"singleton1.value: {singleton1.value}")  # Вывод: "Первый экземпляр"
    print(f"singleton2.value: {singleton2.value}")  # Вывод: "Первый экземпляр"

    # Изменим значение через один из экземпляров
    singleton1.value = "Обновленный экземпляр"

    print("\nСостояние экземпляров после изменения:")
    print(f"singleton1.value: {singleton1.value}")  # Вывод: "Обновленный экземпляр"
    print(f"singleton2.value: {singleton2.value}")  # Вывод: "Обновленный экземпляр"
