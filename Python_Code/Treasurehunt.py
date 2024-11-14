# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:43:14 2024

@author: kayla
"""

player_health = 100
player_score = 0
steps = 0

def choose_right():
    global player_score
    global player_health
    global steps
    print("You chose the right path!")
    # Implement logic for the right path (e.g., find treasure, gain points, etc.)
    # Adjust player's score accordingly
    ### BEGIN SOLUTION
    if steps % 2 == 0:
        print("Encounter a wild creature!")
        player_health -= 30
    else:
        print("Discover hidden treasure!")
        player_score += 50
    ### END SOLUTION
    steps+=1
    
def choose_left():
    global player_score
    global player_health
    global steps
    print("You chose the left path!")
    # Implement logic for the left path (e.g., encounter obstacle, lose health, etc.)
    # Adjust player's health accordingly
    ### BEGIN SOLUTION
    if steps % 2 == 0:
        print("Found a secret shortcut!")
        player_score += 20
    else:
        print("Encounter a hidden trap!")
        player_health -= 20
    ### END SOLUTION
    steps+=1
    
def make_choice(direction):
    """
    Simulate the player making a choice in the game.

    Parameters:
    - direction (str): The direction chosen by the player (e.g., "left", "right").

    Returns:
    - Tuple with updated player_health and player_score.
    """
    global player_health, player_score

    if direction == "right":
        choose_right()
    elif direction == "left":
        choose_left()
    else:
        print("Invalid choice. Try again.")

    return player_health, player_score



def play():
    global player_health, player_score, steps
    player_health = 100
    player_score = 0
    steps = 0
    print("Welcome to the Treasure Hunt Game!")

    # Game loop
    while player_health > 0:
        print(f"\nCurrent Step: {steps}")
        print(f"Current Health: {player_health}")
        print(f"Current Score: {player_score}")

        user_choice = input("Choose a direction ('left' or 'right'): ").lower()
        player_health, player_score = make_choice(user_choice)
    
        
        #Add your logic here for handling players winning the game
        ### BEGIN SOLUTION
               
        if player_score >= 150:
            print("Congratulations, treasure Found!")
            print("\nGame Over! Thanks for playing.")
            break

        ### END SOLUTION

    else: print("\nGame Over! Thanks for playing.")


if(__name__=='__main__'):
    play()     #To test the functionality of your game