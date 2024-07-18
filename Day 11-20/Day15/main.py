MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"money: ${cash}")


def check(coffee_type):
    ingredients = MENU[coffee_type]['ingredients']

    if ingredients['water'] > resources['water']:
        print('insufficient water capacity')
        return False
    elif 'milk' in ingredients and ingredients['milk'] > resources['milk']:
        print('insufficient milk capacity')
        return False
    elif ingredients['coffee'] > resources['coffee']:
        print('insufficient coffee capacity')
        return False
    else:
        return True


def sale(coffee_type):
    ingredients = MENU[coffee_type]['ingredients']

    resources["water"] -= ingredients['water']

    if 'milk' in ingredients:
        resources["milk"] -= ingredients['milk']

    resources["coffee"] -= ingredients['coffee']

    return resources


def calc(quarters, dimes, nickels, pennies):
    a = quarters * 0.25
    b = dimes * 0.10
    c = nickels * 0.05
    d = pennies * 0.01
    return a + b + c + d


is_off = False

cash = 0

while not is_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    while user_choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
        user_choice = input("Item not available, please input espresso/latte/cappuccino").lower()

    if user_choice == 'off':
        is_off = True

    elif user_choice == 'report':
        report()

    else:
        if check(user_choice):
            print('Please insert coins')

            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))
            nickels = int(input('How many nickels?: '))
            pennies = int(input('How many pennies?: '))
            user_total = calc(quarters, dimes, nickels, pennies)

            if user_total >= MENU[user_choice]['cost']:
                change = user_total - MENU[user_choice]['cost']
                resources = sale(user_choice)
                cash += MENU[user_choice]['cost']
                print(f'Here is your {user_choice}☕, Enjoy!\nYour change is ${change:.2f}')
            else:
                print('Not enough money, refunded')
