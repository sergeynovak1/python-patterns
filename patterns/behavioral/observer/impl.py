class Subject:
    """Интерфейс для объектов, за которыми следят наблюдатели."""

    def __init__(self):
        """Инициализация списка наблюдателей."""
        self._observers = []

    def attach(self, observer):
        """Добавляет наблюдателя.

        Args:
            observer (Observer): наблюдатель, который будет добавлен.
        """
        self._observers.append(observer)

    def detach(self, observer):
        """Удаляет наблюдателя.

        Args:
            observer (Observer): наблюдатель, который будет удален.
        """
        self._observers.remove(observer)

    def notify(self):
        """Уведомляет всех наблюдателей об изменении состояния."""
        for observer in self._observers:
            observer.update(self)


class ConcreteSubject(Subject):
    """Конкретный объект, за состоянием которого следят."""

    def __init__(self):
        """Инициализация состояния."""
        super().__init__()
        self._state = None

    @property
    def state(self):
        """Возвращает текущее состояние."""
        return self._state

    @state.setter
    def state(self, value):
        """Устанавливает новое состояние и уведомляет наблюдателей.

        Args:
            value: новое состояние.
        """
        self._state = value
        self.notify()


class Observer:
    """Интерфейс для наблюдателей."""

    def update(self, subject):
        """Вызывается для уведомления об изменении состояния объекта Subject.

        Args:
            subject (Subject): объект, за которым следит наблюдатель.
        """
        pass


class ConcreteObserver(Observer):
    """Конкретный наблюдатель, который получает обновления от объекта Subject."""

    def update(self, subject):
        """Реакция на изменение состояния объекта Subject.

        Args:
            subject (Subject): объект, за которым следит наблюдатель.
        """
        print(f"Observer notified. New state: {subject.state}")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.state = "State 1"  # Уведомляет всех наблюдателей
    subject.state = "State 2"  # Уведомляет всех наблюдателей
