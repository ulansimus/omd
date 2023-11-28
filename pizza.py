from typing import Dict, List


class Pizza:
    """
    Класс, используемый для предоставления пиццы. В пиццу входит название, ингредиенты, размер.

    ...

    Атрибуты
    ---------
    name : str
        название пиццы
    toppings : List[str]
        список ингредиентов пиццы
    size : str
        размер пиццы(L или XL)
    other : Pizza
        другая пицца такого же класса

    Методы
    -------
    __init__(name, toppings, size)
        инициализирует пиццу
    dict()
        возвращает данные о пицце в виде словаря с ключом - название пиццы,
        значением - список ингредиентов пиццы
    __eq__(other)
        принимает другую пиццу и сравнивает пиццы на идентичность
    """

    def __init__(self, name: str, toppings: List[str], size: str = 'L') -> None:
        """Инициализирует пиццу."""

        if not isinstance(size, str):
            raise TypeError('size in string')
        self.name = name
        self.toppings = toppings
        self.size = size

    def dict(self) -> Dict[str, list]:
        """
        Возвращает рецепт пиццы в виде словаря с ключом - название пиццы,
        значением - список ингредиентов пиццы.
        """

        return {self.name: self.toppings}

    def __eq__(self, other) -> bool:
        """Принимает другую пиццу и сравнивает пиццы на идентичность."""

        return (
            isinstance(other, self.__class__) and
            self.toppings == other.toppings and
            self.size == other.size
        )
