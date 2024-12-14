from abc import ABC, abstractmethod


# Интерфейс команды
class Command(ABC):
    """Абстрактный класс команды."""

    def __init__(self):
        self.is_complete = False

    @abstractmethod
    def execute(self):
        pass


# Конкретные команды
class LightOnCommand(Command):
    """Конкретная команда для включения света."""

    def __init__(self, light):
        super().__init__()
        self.light = light

    def execute(self):
        self.light.on()
        self.is_complete = True


class LightOffCommand(Command):
    """Конкретная команда для выключения света."""

    def __init__(self, light):
        super().__init__()
        self.light = light

    def execute(self):
        self.light.off()
        self.is_complete = True


class ACOnCommand(Command):
    """Конкретная команда для включения кондиционера."""

    def __init__(self, ac):
        super().__init__()
        self.ac = ac

    def execute(self):
        self.ac.on()
        self.is_complete = True


class ACOffCommand(Command):
    """Конкретная команда для выключения кондиционера."""

    def __init__(self, ac):
        super().__init__()
        self.ac = ac

    def execute(self):
        self.ac.off()
        self.is_complete = True


# Получатели
class Light:
    """Класс, представляющий свет."""

    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")


class AirConditioner:
    """Класс, представляющий кондиционер."""

    def on(self):
        print("AirConditioner is ON")

    def off(self):
        print("AirConditioner is OFF")


# Транзакционный менеджер
class TransactionManager:
    """Класс, управляющий транзакциями команд."""

    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

    def get_transaction_status(self):
        return all(command.is_complete for command in self.commands)


# Клиентский код
if __name__ == "__main__":
    # Создаем получателей
    light = Light()
    ac = AirConditioner()

    # Создаем команды
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    ac_on = ACOnCommand(ac)
    ac_off = ACOffCommand(ac)

    # Создаем транзакционный менеджер и добавляем команды
    transaction_manager = TransactionManager()
    transaction_manager.add_command(light_on)
    transaction_manager.add_command(ac_on)
    transaction_manager.add_command(light_off)
    transaction_manager.add_command(ac_off)

    # Выполняем команды
    transaction_manager.execute_commands()

    # Проверяем статус транзакции
    if transaction_manager.get_transaction_status():
        print("All commands executed successfully.")
    else:
        print("Some commands were not executed successfully.")
