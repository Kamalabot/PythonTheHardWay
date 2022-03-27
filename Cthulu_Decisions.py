print("""You ente a dark room with 2 doors.
Do you go through door 1 or 2?""")

door = input("> ")

if door == '1':
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1.Take the cake")
    print("2.Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("Bear eats your legs off. Good Job!")

    else:
        print(f"Well. doing {bear} is probably better")
        print("Bear runs away")

elif door == '2':
    print("You stare into the endless abyss of Cthulu's retina")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understand revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == '2':
        print("Your body survives powered by mind of jello")

    else: 
        print("The insanity rots your eyes into pool of muck.")

else:
    print("You stumble around and fall on a knife and die.")