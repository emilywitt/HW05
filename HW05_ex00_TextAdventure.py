#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
from sys import argv

# Body

def infinite_stairway_room(count,name):
    print name + " walks through the door to see a dimly lit hallway."
    print "At the end of the hallway is a" + (count * 'long ') + 'staircase going towards some light. What does ' + name + " do?"    
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print name + ' takes the stairs'
        if (count > 0):
            print "but " + name + " is not happy about it"
        infinite_stairway_room(count + 1, name)
    # option 2 == ?????
    if next == "turn around":
        print name + " goes back to the gold room."
        gold_room(name)
        

def gold_room(name):
    print "This room is full of gold.  How much does " + name + " take?"
    while True:
        how_much = raw_input("> ")
        try:
            how_much == int(how_much)
            if int(how_much) > 50:
                print name + " is greedy. after taking the gold, "
                infinite_stairway_room(int(how_much),name)
            elif int(how_much) <= 50:
                print "You have a heart of gold! Since you're not greedy, you win!"
                pass
        except:
            print "Come on, " + name + ", type a number." 
    exit(0)   

def bear_room(name):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is " + name + " going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey" or next == "take" or next == "honey":
            dead("The bear looks at " + name + " then slaps " + name + "'s face off.")
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. " + name + " can go through it now."
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews " + name + "'s leg off.")
        elif (next == "open" or next == "door") and bear_moved:
            gold_room(name)
        else:
            print "I got no idea what that means."


def cthulhu_room(name):
    print "Here " + name + " sees the great evil Cthulhu."
    print "He, it, whatever stares at " + name + " and " + name + " goes insane."
    print "Does " + name + " flee for his/her life or eat his/her own head?"

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Dead!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    name = argv[1]
    print name + " is in a dark room."
    print "There is a door to " + name + "'s right and left."
    print "Which one does " + name + " take?"

    next = raw_input("> ")

    if next == "left":
        bear_room(name)
    elif next == "right":
        cthulhu_room(name)
    else:
        dead(name + " stumbles around the room and then starves.")

if __name__ == '__main__':
    main()
