# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Product:
    def init(self, product_name: str, price: float):
        """
        Создание и подготовка к работе объекта "Товар".
        :param product_name: Название товара
        :param price: Цена товара
        Примеры:
        >>> product_item = Product("Laptop", 1200.0)  # инициализация экземпляра класса
        """
        if not isinstance(product_name, str):
            raise TypeError("Название товара должно быть строкой")
        self.product_name = product_name

        if not isinstance(price, (int, float)):
            raise TypeError("Цена товара должна быть числом")
        if price < 0:
            raise ValueError("Цена товара не может быть отрицательным числом")
        self.price = price

    def get_price(self) -> float:
        """
        Получение текущей цены товара.
        :return: Текущая цена товара
        Примеры:
        >>> product_item = Product("Laptop", 1200.0)
        >>> product_item.get_price()
        1200.0
        """
        return self.price

    def apply_discount(self, discount_amount: float) -> float:
        """
        Применение скидки к цене товара.
        :param discount_amount: Сумма скидки
        :return: Новая цена после применения скидки
        Примеры:
        >>> product_item = Product("Laptop", 1200.0)
        >>> product_item.apply_discount(200.0)
        1000.0
        """
        if not isinstance(discount_amount, (int, float)):
            raise TypeError("Сумма скидки должна быть числом")
        if discount_amount < 0:
            raise ValueError("Сумма скидки не может быть отрицательной")
        self.price -= discount_amount
        return self.price


class RecipeIngredient:
    def init(self, ingredient_name: str, quantity: float):
        """
        Создание и подготовка к работе объекта "Ингредиент рецепта".
        :param ingredient_name: Название ингредиента
        :param quantity: Количество ингредиента
        Примеры:
        >>> recipe_ingredient = RecipeIngredient("Flour", 2.0)  # инициализация экземпляра класса
        """
        if not isinstance(ingredient_name, str):
            raise TypeError("Название ингредиента должно быть строкой")
        self.ingredient_name = ingredient_name

        if not isinstance(quantity, (int, float)):
            raise TypeError("Количество ингредиента должно быть числом")
        if quantity < 0:
            raise ValueError("Количество ингредиента не может быть отрицательным числом")
        self.quantity = quantity

    def get_quantity(self) -> float:
        """
        Получение текущего количества ингредиента.
        :return: Текущее количество ингредиента
        Примеры:
        >>> recipe_ingredient = RecipeIngredient("Flour", 2.0)
        >>> recipe_ingredient.get_quantity()
        2.0
        """
        return self.quantity


class ElectronicDevice:
    def init(self, brand: str, model: str, year: int, storage_capacity: int, battery_life: float):
        """
        Создание и подготовка к работе объекта "Электронное устройство".
        :param brand: Бренд электронного устройства
        :param model: Модель электронного устройства
        :param year: Год выпуска электронного устройства
        :param storage_capacity: Объем памяти электронного устройства в гигабайтах
        :param battery_life: Время автономной работы батареи в часах
        Примеры:
        >>> electronic_device = ElectronicDevice("Apple", "iPhone 13", 2021, 256, 12.5)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд электронного устройства должен быть строкой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель электронного устройства должна быть строкой")
        self.model = model

        if not isinstance(year, int) or year < 2000:
            raise ValueError("Год выпуска электронного устройства должен быть положительным целым числом после 2000 года")
        self.year = year
        if not isinstance(storage_capacity, int) or storage_capacity <= 0:
            raise ValueError("Объем памяти электронного устройства должен быть положительным целым числом")
        self.storage_capacity = storage_capacity

        if not isinstance(battery_life, (int, float)) or battery_life <= 0:
            raise ValueError("Время автономной работы батареи должно быть положительным числом")
        self.battery_life = battery_life

    def get_device_info(self) -> str:
        """
        Получение информации об электронном устройстве.
        :return: Строка с информацией об электронном устройстве
        Примеры:
        >>> electronic_device = ElectronicDevice("Apple", "iPhone 13", 2021, 256, 12.5)
        >>> electronic_device.get_device_info()
        'Apple iPhone 13 (2021), 256GB, Battery Life: 12.5 hours'
        """
        return f'{self.brand} {self.model} ({self.year}), {self.storage_capacity}GB, Battery Life: {self.battery_life} hours'

    if name == "main":
        doctest.testmod()  # тестирование примеров, которые находятся в документации