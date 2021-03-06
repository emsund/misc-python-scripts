"""
Simulation of the "vaunted Monty Hall problem"
Mar 7, 2017
"""
# Trusting Monty (switching doors when he offers) is the winning strategy.
trust_monty = True 

max_rounds = 10000
goats_won = 0
cars_won = 0
i = 0

import random

while i <= max_rounds:
    doors = ["goat","goat","car"]
    random.shuffle(doors)
    choice = doors.pop()
    doors.remove("goat") # Monty makes his choice - he MUST reveal a goat, not a car.

    if trust_monty:
        choice = doors[0] # uncomment this to switch to the winning strategy (trusting Monty)
    
    # add to our total winnings
    if choice == "goat":
        goats_won += 1
        print("Goat...")
    elif choice == "car":
        cars_won += 1
        print("CAR!!!")

    i += 1


print("Percent goats won: ",(goats_won/max_rounds)*100,"%")
print("Percent cars won: ",(cars_won/max_rounds)*100,"%")

################## OLD CODE ###############################

def generate_setup():
    """ Pseudorandomly place 2 goats and 1 car behind 3 doors. Return door list. """
    
    import random
    
    doors = ["goat","goat","car"]
    #doors = [1,2,3]
    #prizes = ["goat","goat","car"]
    random.shuffle(doors)
    
    return doors

def make_first_choice():
    """ Given the three closed doors, choose one. (Return index of chosen door.) """

    first_choice = doors.pop()
    
    return first_choice

def monty_choose(remaining_doors, first_choice):
    """ Monty reveals a door from remaining two. He will never reveal a car. """
    
    remaining_doors.remove("goat")
    
    first_choice
    monty_choice
    final_choice
    
    return remaining_doors

def take_offer(remaining_doors):
    """ When Monty offers switching your door choice, switch. """

    choice = doors[0]

def reject_offer(doors):
    """ When Monty offers switching your door choice, stick with first choice. """

    choice = first_choice
    
    return choice

def reveal(doors):
    """ Reveal the contents of chosen door. """
    print(doors)
