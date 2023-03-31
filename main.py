from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 
from art import logo

menu = Menu()
money = MoneyMachine()
coffee =  CoffeeMaker()

machine_working = True
while machine_working:
    print(logo)
    items = menu.get_items()
    users_choice = input(f"Enter your choice = {items}")
    
    if users_choice == "turn-off":
        machine_working =  False
    elif users_choice == "give-report":
        coffee.report()
        money.report()
    else:
        give_drink = menu.find_drink(users_choice)
        # idk why theres an error showing in my linter but the code works just fine the "cost" is a member of menu in __init__
        if coffee.is_resource_sufficient(give_drink) and money.make_payment(give_drink.cost):
            coffee.make_coffee(give_drink)



