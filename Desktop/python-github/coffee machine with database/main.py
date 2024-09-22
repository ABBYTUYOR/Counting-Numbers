from database import *
from prettytable import PrettyTable
from time import sleep
from art import counting, logo
from coin import get_coin
from database import resources_command, menu, resources

connection_command()

print(logo)
keep_on_running = True

while keep_on_running:
    table = PrettyTable()
    table.add_column('Products', ['Espresso', 'Latte', 'Cappuccino'])
    table.add_column('Price', ['$1.5', '$2.5', '$3.0'])
    table.align['Products'] = 'l'
    print(table)
    customer_choice = input("What would you like? ").title()

    if customer_choice == 'Report':
        select_command()

    elif customer_choice == 'Resources':
        update_command(500, 500, 500)

    elif customer_choice == 'off':
        keep_on_running = False

    else:

        if customer_choice == 'Espresso':

            resources_list = resources_command()

            total = get_coin()
            deducted_water = resources_list[0] - menu[0]['Espresso']['Water']
            deducted_coffee = resources_list[1] - menu[0]['Espresso']['Coffee']
            change = total - menu[0]['Cost']

            if total < menu[0]['Cost']:
                print(f"\nSorry that's not enough money.${round(total, 2)} refunded.\n")
            elif resources_list[0] < menu[0]['Espresso']['Water']:
                print("\nSorry there is not enough water.\n")
            elif resources_list[1] < menu[0]['Espresso']['Coffee']:
                print("\nSorry there is not enough coffee.\n")
            else:

                deduction_command(deducted_water, deducted_coffee, resources_list[2], resources_list[3] + menu[0]['Cost'])

                for i in counting:
                    print(i)
                    sleep(1)

                receipts = PrettyTable()
                receipts.add_column(f"Here is ${round(change, 2)} dollars in change.", ["Here is your espresso ☕. Enjoy!"])
                print(receipts)

        elif customer_choice == 'Latte':

            resources_list = resources_command()

            total = get_coin()

            deducted_water = resources_list[0] - menu[1]['Latte']['Water']
            deducted_coffee = resources_list[1] - menu[1]['Latte']['Coffee']
            deducted_milk = resources_list[2] - menu[1]['Latte']['Milk']
            change = total - menu[1]['Cost']

            if total < menu[1]['Cost']:
                print(f"\nSorry that's not enough money.${round(total, 2)} refunded.\n")

            elif resources_list[0] < menu[1]['Latte']['Water']:
                print("\nSorry there is not enough water.\n")

            elif resources_list[1] < menu[1]['Latte']['Coffee'] :
               print("\nSorry there is not enough coffee.\n")

            elif  resources_list[2] < menu[1]['Latte']['Milk']:
                print("\nSorry there is not enough Milk.\n")

            else:

                deduction_command(deducted_water, deducted_coffee, deducted_milk, resources_list[3] + menu[1]['Cost'])

                for i in counting:
                    print(i)
                    sleep(1)

                receipts = PrettyTable()
                receipts.add_column(f"Here is ${round(change, 2)} dollars in change.", ["Here is your espresso ☕. Enjoy!"])
                print(receipts)

        elif customer_choice == 'Cappuccino':

            resources_list = resources_command()

            total = get_coin()

            deducted_water = resources_list[0] - menu[2]['Cappuccino']['Water']
            deducted_coffee = resources_list[1] - menu[2]['Cappuccino']['Coffee']
            deducted_milk = resources_list[2] - menu[2]['Cappuccino']['Milk']
            change = total - menu[2]['Cost']

            if total < menu[2]['Cost']:
                print(f"\nSorry that's not enough money.${round(total, 2)} refunded.\n")

            elif resources_list[0] < menu[2]['Cappuccino']['Water']:
                print("\nSorry there is not enough water.\n")

            elif resources_list[1] < menu[2]['Cappuccino']['Coffee']:
                print("\nSorry there is not enough coffee.\n")

            elif resources_list[2] < menu[2]['Cappuccino']['Milk']:
                print("\nSorry there is not enough Milk.\n")

            else:

                deduction_command(deducted_water, deducted_coffee, deducted_milk, resources_list[3] + menu[2]['Cost'])

                for i in counting:
                    print(i)
                    sleep(1)

                receipts = PrettyTable()
                receipts.add_column(f"Here is ${round(change, 2)} dollars in change.", ["Here is your espresso ☕. Enjoy!"])
                print(receipts)




