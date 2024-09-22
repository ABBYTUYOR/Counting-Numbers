from prettytable import PrettyTable


def get_coin():
    #coins amount for a change.
    quarter_counter = int(input("How many quarter: ")) * 0.50
    dime_counter = int(input("How many dimes: ")) * 0.10
    nickel_counter = int(input("How many nickels: ")) * 0.05
    penny_counter = int(input("How many penny: ")) * 0.01
    return quarter_counter + dime_counter + nickel_counter + penny_counter
