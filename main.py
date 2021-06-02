MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

money = []


def start():
    user_answer = input("what would you like? (espresso/latte/cappuccino)")
    if user_answer == "report":
        return report()
    elif user_answer == "off":
        return
    elif user_answer == "espresso" or user_answer == "latte" or user_answer == "cappuccino":
        check_resource(user_answer)
        pay(user_answer)
    else:
        return()


def report():
    print(f"water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {sum(money)}")
    return start()


def check_resource(user_answer):
    for remain in resources:
        if resources[remain] < MENU[user_answer]["ingredients"][remain]:
            print(f"Sorry there is not enough {remain}")
            return start()


def pay(user_answer):
    print("Please insert coins.")
    quarter = float(input("how many quarters?: "))
    dime = float(input("how many dimes?: "))
    nickel = float(input("how many nickels?: "))
    penny = float(input("how many pennies?: "))
    total_received = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    if total_received > MENU[user_answer]["cost"]:
        cal = round(total_received - MENU[user_answer]['cost'], 2)
        money.append(MENU[user_answer]["cost"])
        print(f"Here is ${cal} in change. ")
        print(f"Here is your {user_answer} ☕ Enjoy!")
        subtract(user_answer)
        return start()
    else:
        print("not enough money money refunded")
        return start()


def subtract(user_answer):
    for ingredient in resources:
        resources[ingredient] = resources[ingredient] - MENU[user_answer]["ingredients"][ingredient]


start()