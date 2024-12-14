# Подсистемы
class TV:
    """Класс, представляющий телевизор."""

    def on(self):
        print("TV is ON")

    def off(self):
        print("TV is OFF")

    def set_channel(self, channel):
        print(f"TV channel set to {channel}")


class SoundSystem:
    """Класс, представляющий аудиосистему."""

    def on(self):
        print("Sound system is ON")

    def off(self):
        print("Sound system is OFF")

    def set_volume(self, volume):
        print(f"Sound system volume set to {volume}")


class DVDPlayer:
    """Класс, представляющий проигрыватель дисков."""

    def on(self):
        print("DVD Player is ON")

    def off(self):
        print("DVD Player is OFF")

    def play(self, movie):
        print(f"Playing movie: {movie}")


# Фасад
class HomeTheaterFacade:
    """Фасад для управления домашним кинотеатром."""

    def __init__(self, tv: TV, sound_system: SoundSystem, dvd_player: DVDPlayer):
        self.tv = tv
        self.sound_system = sound_system
        self.dvd_player = dvd_player

    def watch_movie(self, movie):
        """Метод для подготовки домашнего кинотеатра к просмотру фильма."""
        print("Get ready to watch a movie...")
        self.tv.on()
        self.sound_system.on()
        self.dvd_player.on()
        self.tv.set_channel(3)
        self.sound_system.set_volume(15)
        self.dvd_player.play(movie)

    def end_movie(self):
        """Метод для завершения просмотра фильма и выключения всех устройств."""
        print("Shutting down home theater...")
        self.tv.off()
        self.sound_system.off()
        self.dvd_player.off()


# Клиентский код
if __name__ == "__main__":
    tv = TV()
    sound_system = SoundSystem()
    dvd_player = DVDPlayer()
    home_theater = HomeTheaterFacade(tv, sound_system, dvd_player)

    home_theater.watch_movie("Inception")
    # Вывод:
    # Get ready to watch a movie...
    # TV is ON
    # Sound system is ON
    # DVD Player is ON
    # TV channel set to 3
    # Sound system volume set to 15
    # Playing movie: Inception

    home_theater.end_movie()
    # Вывод:
    # Shutting down home theater...
    # TV is OFF
    # Sound system is OFF
    # DVD Player is OFF
