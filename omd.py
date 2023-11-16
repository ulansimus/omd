import click
from typing import Dict, List
from random import randint


class Pizza:
    """Пицца - в нее входит название, ингредиенты"""
    def __init__(self, name: str, toppings: List[str]) -> None:
        self.name = name
        self.toppings = toppings

    def dict(self) -> Dict[str, list]:
        return {self.name: self.toppings}

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.toppings == other.toppings


def display_menu(pizzas: dict[str, list[str]]) -> None:
    """печатает меню"""
    for pizza in pizzas:
        toppings = ', '.join(pizzas[pizza])
        print(f"- {pizza}: {toppings}")


def prepare_pizza(pizza: Pizza, delivery=False) -> None:
    """ печатает время приготовления и доставки"""
    if delivery:
        s = randint(5, 15)
        print(f"Приготовим за {s}m")
        s = randint(5, 15)
        print(f"Доставим за {s}m")
    else:
        s = randint(5, 15)
        print(f"Приготовим за {s}m")


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Предоставляет меню пицц с их ингредиентами"""
    menu = {
        "Margherita ": ["tomato sauce", "mozzarella", "tomatoes"],
        "Pepperoni ": ["tomato sauce", "mozzarella", "pepperoni"],
        "Hawaiian ": ["tomato sauce", "mozzarella", "chicken", "pineapples"]
    }
    display_menu(menu)


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """ Выполнение команды order, приготовление пиццы и ее доставка(если указан флаг)"""
    menu = {
        "Margherita": ["tomato sauce", "mozzarella", "tomatoes"],
        "Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"],
        "Hawaiian": ["tomato sauce", "mozzarella", "chicken", "pineapples"]
    }
    if pizza in menu:
        selected_pizza = Pizza(pizza, menu[pizza])
        prepare_pizza(selected_pizza, delivery)
    else:
        print("Этой пиццы нет в меню")


if __name__ == '__main__':
    cli()
