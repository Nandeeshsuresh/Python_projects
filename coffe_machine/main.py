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

coffee_money=0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cappuccino = MENU["cappuccino"]
espresso = MENU["espresso"]
latte = MENU["latte"]


def resource_checker(type_of_coffee):
    if resources["water"] >= type_of_coffee["ingredients"]["water"]:
        if resources["milk"] >= type_of_coffee["ingredients"]["milk"]:
            if resources["coffee"] >= type_of_coffee["ingredients"]["coffee"]:
                return False
            else:
                print(" Sorry there is not enough coffee powder.")
                return True
        else:
            print(" Sorry there is not enough milk powder.")
            return True
    else:
        print(" Sorry there is not enough water.")
        return True


def espresso_resource_checker(type_of_coffee):
    if resources["water"] >= type_of_coffee["ingredients"]["water"]:
        if resources["coffee"] >= type_of_coffee["ingredients"]["coffee"]:
            return False
        else:
            print(" Sorry there is not enough coffee powder")
            return True
    else:
        print(" Sorry there is not enough water")
        return True


# resource_checker = resource_checker(type_of_coffee)

def insert_coins():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickels?: "))
    pennies = float(input("how many pennies?: "))
    return quarters, dimes, nickles, pennies


run_coffee_machine = True
while run_coffee_machine:
    def which_coffee():
        type_of_coffee = input(" What would you like ? (espresso/latte/cappuccino): ")
        return type_of_coffee


    checking_resource = True
    while checking_resource:
        type_of_coffee = which_coffee()
        if type_of_coffee == "espresso":
            type_of_coffee = MENU[type_of_coffee]
            checking_resource = espresso_resource_checker(espresso)
        elif type_of_coffee == "cappuccino":
            type_of_coffee = MENU[type_of_coffee]
            checking_resource = resource_checker(type_of_coffee)
        elif type_of_coffee == "latte":
            type_of_coffee = MENU[type_of_coffee]
            checking_resource = resource_checker(type_of_coffee)
        elif type_of_coffee == "report":
            checking_resource = False
        elif type_of_coffee == "off":
            checking_resource = False
        else:
            print("Enter the correct input.")

    if type_of_coffee == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${coffee_money}")

    elif type_of_coffee == cappuccino:
        coins = list(insert_coins())
        quarters_in_dollars = coins[0] * .25
        dimes_in_dollars = coins[1] * 0.10
        nickles_in_dollars = coins[2] * 0.05
        pennies_in_dollars = coins[3] * 0.01

        coins_in_dollars = quarters_in_dollars + dimes_in_dollars + nickles_in_dollars + pennies_in_dollars


    elif type_of_coffee == espresso:
        coins = list(insert_coins())
        quarters_in_dollars = coins[0] * .25
        dimes_in_dollars = coins[1] * 0.10
        nickles_in_dollars = coins[2] * 0.05
        pennies_in_dollars = coins[3] * 0.01

        coins_in_dollars = quarters_in_dollars + dimes_in_dollars + nickles_in_dollars + pennies_in_dollars


    elif type_of_coffee == latte:
        coins = list(insert_coins())
        quarters_in_dollars = coins[0] * .25
        dimes_in_dollars = coins[1] * 0.10
        nickles_in_dollars = coins[2] * 0.05
        pennies_in_dollars = coins[3] * 0.01

        coins_in_dollars = quarters_in_dollars + dimes_in_dollars + nickles_in_dollars + pennies_in_dollars


    elif type_of_coffee == "off":
        exit()

    if type_of_coffee != "report":
        if type_of_coffee == cappuccino and coins_in_dollars >= cappuccino["cost"]:
            change = round(coins_in_dollars - cappuccino["cost"], 2)
            coffee_money+=cappuccino["cost"]
            print(f"Here is ${change} in change")
            print("Here is your cappuccino ☕. Enjoy!")
            resources["water"] = resources["water"] - cappuccino["ingredients"]["water"]
            resources["milk"] = resources["milk"] - cappuccino["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - cappuccino["ingredients"]["coffee"]

        elif type_of_coffee == espresso and coins_in_dollars >= espresso["cost"]:
            change = round(coins_in_dollars - espresso["cost"], 2)
            coffee_money += espresso["cost"]
            print(f"Here is ${change} in change")
            print("Here is your espresso ☕. Enjoy!")
            resources["water"] = resources["water"] - espresso["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - espresso["ingredients"]["coffee"]

        elif type_of_coffee == latte and coins_in_dollars >= latte["cost"]:
            change = round(coins_in_dollars - latte["cost"], 2)
            coffee_money += latte["cost"]
            print(f"Here is ${change} in change")
            print("Here is latte ☕. Enjoy!")
            resources["water"] = resources["water"] - latte["ingredients"]["water"]
            resources["milk"] = resources["milk"] - latte["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - latte["ingredients"]["coffee"]

        elif coins_in_dollars <= cappuccino["cost"]:
            print("Sorry that's not enough money. Money refunded.")

        elif coins_in_dollars <= latte["cost"]:
            print("Sorry that's not enough money. Money refunded.")

        elif coins_in_dollars <= espresso["cost"]:
            print("Sorry that's not enough money. Money refunded.")





