# coffee machine task

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

profit = 0


machine_on = True


def insert_coins(drink_total_cost):
    print(f'Your total is {drink_total_cost}, please insert coins now')
    quarters_inserted = int(input('How many quarters? ')) * 0.25
    dimes_inserted = int(input('How many dimes? ')) * 0.10
    nickles_inserted = int(input('How many nickles? ')) * 0.05
    pennies_inserted = int(input('How many pennies? ')) * 0.01
    total = (quarters_inserted + dimes_inserted + nickles_inserted + pennies_inserted)

    change = total - drink_total_cost

    if total > drink_total_cost:
        print(f'Thanks for your payment, your change is {change}')
    else:
        print('No change given, enjoy your coffee')


def is_resource_sufficient(order_ingredients, drink_total):
    print(order_ingredients)
    if (order_ingredients['water'] < resources['water'] and
            order_ingredients['coffee'] < resources['coffee']):
        insert_coins(drink_total)




while machine_on:
    user_choose = input('What would you like? (espresso/latte/cappuccino) ')
    if user_choose == 'off':
        machine_on = False
    elif user_choose == 'report':
        print(f'Water: {resources['water']}ml')
        print(f'Milk: {resources['milk']}ml')
        print(f'Coffee: {resources['coffee']}ml')
        print(f'Money: ${profit}')
    else:
        drink = MENU[user_choose]
        drink_cost = MENU[user_choose]['cost']
        if is_resource_sufficient(drink["ingredients"], drink_cost):
            print('yes')

            # milk_deducted = resources['milk'] - MENU[user_choose]['ingredients']['milk']
            # resources['milk'] = milk_deducted
        #
        # else:
        #     print('sorry there is not enough resources left :(, please choose another drink')
