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

money = 0


def start():
    user_answer = input("what would you like? (espresso/latte/cappuccino)")
    if user_answer == "report":
        report()
    if user_answer == "off":
        return
    if user_answer == "espresso":
        espresso(user_answer)


def espresso(user_answer):
    check_resource(user_answer)
    if pay(user_answer):
        print("Here is your espresso Enjoy!")
        start()
    else:
        print("merong")




def report():
    print(f"water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")
    start()


def check_resource(user_answer):
    for remain in resources:
        for 
check_resource()

def pay(user_answer):
    print("Please insert coins.")
    quarter = float(input("how many quarters?: "))
    dime = float(input("how many dimes?: "))
    nickel = float(input("how many nickels?: "))
    penny = float(input("how many pennies?: "))
    total_received = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    if total_received > MENU[user_answer]["cost"]:
        cal = round(total_received - MENU[user_answer]['cost'], 2)
        print(f"Here is ${cal} in change. ")
        return True
    else:
        print("not enough money")
        return

