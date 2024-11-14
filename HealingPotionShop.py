# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:40:07 2024

@author: kayla
"""

def display_shop_menu():
    print("=== Healing Potion Shop ===")
    print("1. Buy Healing Potion")
    print("2. Sell Inventory")
    print("3. Exit")
    

def purchase_potions(currency, inventory):    
    potion_cost = 10  # Cost of each healing potion in gold coins

    # Prompt the user to choose the quantity of healing potions
    quantity_str = input("How many potions would you like to buy? ")

    ### BEGIN SOLUTION
    try:
        quantity = int(quantity_str)
        if(quantity < 0): raise Exception
    except (ValueError):
        print("Error: Please enter a valid integer for the quantity.")
        return currency, inventory
    except Exception: 
        print("Error: Please enter a positive quantity.")
        return currency, inventory
   
    try:
        total_cost = quantity * potion_cost
        if total_cost > currency: raise Exception
    except Exception:
        print("Error: Insufficient funds.")
        return currency, inventory
    else:
        currency -= total_cost
        inventory['Healing Potion'] += quantity
    
    
    ### END SOLUTION
    print(f"Purchase successful! Total cost: {total_cost} gold coins")
    print(currency, inventory)
    return currency, inventory

def display_inventory(inventory):
    print("=== Inventory ===")
    for potion, quantity in inventory.items():
        print(f"{potion}: {quantity}")

def sell_inventory(currency, inventory):
    # Display the current inventory
    display_inventory(inventory)

    # Prompt the user to choose the quantity of healing potions to sell
    quantity_str = input("How many potions would you like to sell? ")

    ### BEGIN SOLUTION
    sold_amount = 0
    try:
        quantity = int(quantity_str)
        if(quantity < 0): raise Exception
    except (ValueError):
        print("Error: Please enter a valid integer for the quantity.")
        return currency, inventory
    except Exception: 
        print("Error: Please enter a positive quantity.")
        return currency, inventory
    else:
        try:
            if quantity > inventory['Healing Potion']: raise Exception
        except Exception:
            print("Error: You don't have enough Potions to sell.")
            return currency, inventory
        else:
            sold_amount = quantity * 5
            currency += sold_amount
            inventory['Healing Potion'] -= quantity

    ### END SOLUTION
    
    print(f"Sell successful! Earned: {sold_amount} gold coins")
    return currency, inventory

def main():
    player_currency = 100  # Initial amount of in-game currency
    player_inventory = {"Healing Potion": 0}

    while True:
        display_shop_menu()

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Buy Healing Potion
            player_currency,player_inventory = purchase_potions(player_currency, player_inventory)
        elif choice == "2":
            # Sell Inventory
            player_currency,player_inventory = sell_inventory(player_currency, player_inventory)
        elif choice == "3":
            # Exit
            print("Thank you for visiting the Healing Potion Shop!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()