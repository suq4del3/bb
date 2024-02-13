class Cars:
    """Класс, описывающий автомобили"""

    def __init__(self, horse_power: int, weight: float, wheel_drive: str, brand: str):
        """
        Атрибуты:
        :param horse_power: количество лошадиных сил автомобиля
        :param weight: вес автомобиля
        :param wheel_drive: привод автомобиля
        :param brand: марка авто
        """

        self.horse_power = horse_power
        self.weight = weight
        self.wheel_drive = wheel_drive
        self.brand = brand

    def __str__(self) -> str:
        return f"Информация об автомобиле {self.brand}:\n Кол-во Л.С. : {self.horse_power} |" \
               f"\n Привод : {self.wheel_drive} |\n Вес : {self.weight} |\n\n"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, hp={self.horse_power!r})\n\n"

    def go_reverse(self) -> str:
        """Метод, отвечающий за звуковое сопровождение при движении авто назад"""

        return " *Включается парктроник, издаёт пищaщий звук* "

    def turn_headlights_on(self) -> str:
        """Метод, отвечающий за включение фар"""
        return "Фары включены."


class PassengerCar(Cars):
    """Класс, описывающий легковые автомобили"""

    def __init__(self, horse_power: int, weight: float, wheel_drive: str, brand: str, amount_of_seats: int):
        """
        Атрибуты:
        :param amount_of_seats: количество мест в автомобиле
        """
        super().__init__(horse_power, weight, wheel_drive, brand)
        self.amount_of_seats = amount_of_seats

    def __str__(self) -> str:
        return f"Информация о легковом автомобиле {self.brand}:\n Кол-во Л.С. : {self.horse_power} |" \
               f"\n Привод : {self.wheel_drive} |\n Вес : {self.weight} | \n Кол-во мест: {self.amount_of_seats} |\n\n"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, hp={self.horse_power!r} " \
               f"seats={self.amount_of_seats!r})\n\n"

    def go_reverse(self) -> str:
        return " *Включается парктроник, издаёт пищaщий звук* "

    def turn_headlights_on(self) -> str:
        return "Фары включены."


class Truck(Cars):
    """Класс, описывающий грузовые автомобили"""

    def __init__(self, horse_power: int, weight: float, wheel_drive: str, brand: str, load_capacity: float):
        """
        Атрибуты:
        :param load_capacity: грузоподъемность
        """
        super().__init__(horse_power, weight, wheel_drive, brand)
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        return f"Информация о грузовом автомобиле {self.brand}:\n Кол-во Л.С. : {self.horse_power} |" \
               f"\n Привод : {self.wheel_drive} |\n Вес : {self.weight} | " \
               f"\n Грузоподъемность: {self.load_capacity} |\n\n"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, hp={self.horse_power!r} " \
               f"seats={self.load_capacity!r})\n\n"

    def go_reverse(self) -> str:
        """
         Перегрузка в данном случе необходима для того, чтобы обозначить разницу
        между звуками работы парктроника и специальных динакмиков, устанаввлювабщихся
        на грузовой автомобиль на внешней конструкции (для окружающих людей)
        """

        return "Бип , бип, бип, бип ... (звук для окружающих, предупреждающий о том, что грузовик едет назад)"

    def turn_headlights_on(self) -> str:
        return "Фары включены."


class ConiferousTrees:
    """Класс, описывающий хвойные деревья"""

    def __init__(self, height: float, width: float):
        """
        Атрибуты:
        :param height: высота дерева
        :param width: ширина дерева
        """

        self.height = height
        self.width = width


class FirTree(ConiferousTrees):
    pass


class PineTree(ConiferousTrees):
    pass


if __name__ == "__main__":
    pass