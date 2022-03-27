from sys import exit

def gold_room():
    print("This room is full of gold. How do you take?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    
    #Adding additional condition for numbers less than 10...
    elif int(choice) < 10:
        print("Nice you are not greedy...")
        exit(0)
    
    else:
        dead("Man, learn to type")
    #Apart from 0 and 1, any number will result in else execution..
    
    how_much = int(choice)
    if how_much < 50:
        print("Nice, you are not greedy.")
        exit(0)
    else:
        dead("You greedy bastard")

def bear_room():
    print("There is a bear in the room")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")

    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps you face off.")

        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved, door is there...")
            print("You can go through it now")
            bear_moved = True

        elif choice == 'taunt bear' and bear_moved:
            dead("He is pissed off, and chews your head")

        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("Bear has no idea what to do")

def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it. Whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("Well that was tasty")

    else: 
        cthulhu_room()

def dead(why):
    print(why,'good job!!!')

def start():
    print("You are in a dark room")
    print("There is a door to your right and left.")
    print("which one you take")

    choice = input(">")

    if choice == 'right':
        bear_room()
    elif choice == 'left':
        cthulhu_room()

    else:
        print("You stumble around and starve to death....")

#The program starts with this function call... 
start()