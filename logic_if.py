people = 30
cats = 40
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed")

if people > cats:
    print("Not many cat! World is saved")

if people < dogs:
    print("The world is drooled on")

if people > dogs:
    print("The world is dry")

dogs += 5

#Think about this logic below and the numbers. 
#All three will resolve to true... since it is "Or" equal
if people >= dogs:
    print("People are greater than or equal to dogs")

if people <= dogs:
    print("People are less than or equal to dogs")

if people == dogs:
    print("People are dogs")