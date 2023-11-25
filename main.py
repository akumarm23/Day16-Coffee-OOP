# COFFEE MACHINE using OOPS Concept v0.1
from art import logo
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Print the coffee machine logo
print(logo)

# Create instances of the CoffeeMaker, MoneyMachine, and Menu classes
coffee_maker_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Flag to control the main loop
is_on = True

# Main loop for the coffee machine
while is_on:
    # Get the available menu items
    options = menu.get_items()

    # Get user input for their choice
    choice = input(f"What would you like? ({options}): ")

    # Check user's choice
    if choice == "off":
        # Turn off the coffee machine
        is_on = False
    elif choice == "report":
        # Generate and display a report for the coffee maker and money machine
        coffee_maker_machine.report()
        money_machine.report()
    else:
        # Find the selected drink from the menu
        drink = menu.find_drink(choice)
        
        # Check if there are enough resources and the payment is successful
        if coffee_maker_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make the selected coffee
            coffee_maker_machine.make_coffee(drink)

# END OF CODE
