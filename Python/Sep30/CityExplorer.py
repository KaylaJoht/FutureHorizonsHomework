# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:09:04 2024

@author: kayla
"""

def initialize_character():
    ## BEGIN SOLUTION
    character = {'energy':50, 'money': 0, 'inventory':[]}
    return character
    ## END SOLUTION
 

def initialize_city_layout():
    # Initialize the city layout with default blocks, places, items, and money
    city_layout = [
    {'block': 0, 'name': 'Downtown', 'places': [
        {'name': 'Park', 'items': ['Frisbee', 'Sunscreen'], 'money': 10},
        {'name': 'Cafe', 'items': ['Coffee', 'Pastry'], 'money': 15},
        {'name': 'Bookstore', 'items': ['Book', 'Notebook'], 'money': 5}
    ]},
    
    {'block': 1, 'name': 'Residential Area', 'places': [
        {'name': 'Supermarket', 'items': ['Groceries', 'Snacks'], 'money': 20},
        {'name': 'Gym', 'items': ['Protein Shake', 'Towel'], 'money': 8},
        {'name': 'Library', 'items': ['Novel', 'Magazine'], 'money': 3}
    ]},
    
    {'block': 2, 'name': 'Industrial Zone', 'places': [
        {'name': 'Factory', 'items': ['Toolbox', 'Blueprints'], 'money': 12},
        {'name': 'Warehouse', 'items': ['Pallet Jack', 'Safety Vest'], 'money': 18},
        {'name': 'Lab', 'items': ['Microscope', 'Chemicals'], 'money': 7}
    ]},
    
    {'block': 3, 'name': 'Entertainment District', 'places': [
        {'name': 'Theater', 'items': ['Ticket Stub', 'Popcorn'], 'money': 25},
        {'name': 'Nightclub', 'items': ['Glow Sticks', 'Cocktail Umbrella'], 'money': 30},
        {'name': 'Arcade', 'items': ['Game Token', 'High Score Certificate'], 'money': 10}
    ]},
    
    {'block': 4, 'name': 'Park and Recreation Area', 'places': [
        {'name': 'Zoo', 'items': ['Map', 'Animal Fact Sheet'], 'money': 15},
        {'name': 'Playground', 'items': ['Bouncy Ball', 'Jump Rope'], 'money': 5},
        {'name': 'Sports Field', 'items': ['Soccer Ball', 'Water Bottle'], 'money': 8}
    ]}
    ]
    return city_layout


def display_current_location(city, current_block):
    # Print messages about the character's current location
    print(f"Current Location: {city[current_block]['name']}")
    print(f"Available places:")

    #Use a loop to print out the names of all places on the current block
    ### BEGIN SOLUTION
    place = city[current_block]['places']
    for i,loc in enumerate(place):
        print(place[i]['name'])
    ### END SOLUTION
    

def add_to_inventory(character, item):
    #item is a list of items to add to the character's inventory
    ### BEGIN SOLUTION
    for thing in item:
        character['inventory'].append(thing)
    ### END SOLUTION
    
    
def display_inventory(character):
    print('Current Inventory:')
    #Print all items in the character's inventory
    ### BEGIN SOLUTION
    for item in character['inventory']:
        print(item)
    ### END SOLUTION
    

def display_char_stats(character):
    print(f"Character Energy: {character['energy']}\nCharacter Money: ${character['money']}")
    


def explore_location(character, current_block):
    for place in current_block['places']: #iterates through each place available on a block
        
        ans = input(f"Would you like to search {place['name']}?(Y/N)").lower()
        
        if(ans == "y"): 
            add_to_inventory(character, place['items']) #Add items to our inventory
            
            ### BEGIN SOLUTION
            character['energy'] -= len(place['items'])
            place['items'] = []
            character['money'] += place['money']
            place['money'] = 0
            ### END SOLUTION

            #Print the updated stats of the character after searching specific locations
            print(f"Place: {place['name']}")
            print("STATUS UPDATE:..........")
            display_char_stats(character)
            display_inventory(character)
            print('\n')
            

def take_a_break():
    # Prompt the user to take a break or continue exploring
    answer = input("Would you like to stop? (Y/N): ").lower()
    if(answer == "y"):
        return True
    else: 
        return False
    
    
def main():
    # Call initialize_character and initialize_city_layout to set up the character and city
    character = initialize_character()
    city = initialize_city_layout()
    current_block = 0
    stop=False
    
    # The game will loop until the player's decide to take a break
    # A break should be automatically enforced once a character's energy reachees 0
    while(stop==False):
        # First we will display all required information
        # These functions provide the user with a clear view of the game
        display_char_stats(character)
        print('\n') #To print a new line break in between function print statements
        display_inventory(character)
        print('\n') #To print a new line break in between function print statements
        display_current_location(city,current_block)
        print('\n') #To print a new line break in between function print statements
        

        answer = input("Would you like to search the places on this block (Y/N): ").lower()
        if (answer == 'n'): #Move to the next block
            current_block = (current_block+1)%5
            character['energy']-=1
        
        elif(answer =='y'): #Search the place of user choice
            print("--------------Exploring...... -----------------")
            explore_location(character, city[current_block])
            print("--------------complete-------------------------")

        print("______________________________________________________")
        stop=take_a_break()


# Call the main function to start the program
if __name__ == "__main__":
    main()
