import click
from pizza import Pizza
from decorator import log


MENU = {
    "Margherita": ["tomato sauce", "mozzarella", "tomatoes"],
    "Pepperoni": ["tomato sauce", "mozzarella", "pepperoni"],
    "Hawaiian": ["tomato sauce", "mozzarella", "chicken", "pineapples"]
}


def display_menu() -> None:
    """печатает меню."""
    for pizza in MENU:
        toppings = ', '.join(MENU[pizza])
        print(f"- {pizza}: {toppings}")


@log('Пицца приготовится за')
def bake() -> None:
    """пицца готовится."""
    pass


@log('Доставим пиццу за')
def deliver() -> None:
    """пицца доставляется."""
    pass


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Предоставляет меню пицц с их ингредиентами."""
    display_menu()


@cli.command()
@click.option('--delivery', is_flag=True, help='Deliver the pizza')
@click.argument('pizza', nargs=1)
@click.argument('size', type=str, default='L', nargs=1)
def order(pizza: Pizza, size: str, delivery: bool):
    """
    Предоставляет время приготовление пиццы и ее доставка(если указан флаг)

    Доступные пиццы: маргарита, пепперони, гавайская
    """

    if pizza in MENU:
        selected_pizza = Pizza(pizza, MENU[pizza], size)
        bake(selected_pizza)
        if delivery:
            deliver(selected_pizza)
    else:
        print("Этой пиццы нет в меню")


if __name__ == '__main__':
    cli()
