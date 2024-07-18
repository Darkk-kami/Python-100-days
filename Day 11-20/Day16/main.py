from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_off = False

while not is_off:
    options = menu.get_items()
    user_choice = input(f"What would you like?\n{options}\n:").lower()

    if user_choice == 'off':
        is_off = True

    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        availale = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(availale):  
            if money_machine.make_payment(availale.cost):
                coffee_maker.make_coffee(availale)

