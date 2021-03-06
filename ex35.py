# ex35.py
"""
Exercise 35 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

from sys import exit

def gold_room():
    """This function contains the gold room game logic."""
    
    print "This room is full of gold. How much do you take?"
    
    # get input from the user and make sure they enter a number
    while True:
        choice = raw_input("> ")
    
        if choice.isdigit():
            how_much = int(choice)
            break
        else:
            print "Man, learn to type a number."
    
    # determine the result based on the user's input
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    """This function contains the bear room game logic."""
    
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    
    bear_moved = False
    
    # get input from the user and keep doing so until the user moves on or dies
    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and not bear_moved:
            print "You can't. There is a bear in the way. Remember?"
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    """This function contains the cthulhu room game logic."""
    
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    # get input from the user
    choice = raw_input("> ")
    
    # use the user's input to determine what happens next
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    """
    This is a helper function that prints the reason for the player's death
    and then exits the program.
    """   
    print why, "Good job!"
    exit(0)


def start():
    """This function contains the starting room's game logic."""
    
    print "You are in a dark room."
    print "There is a door to your right and your left."
    print "Which one do you take?"
    
    # get input from the user
    choice = raw_input("> ")
    
    # use the user's input to determine what happen's next
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


# call the start() function to start the game
start()

