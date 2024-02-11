people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")

elif cars < people:
    print("People should not take cars.")

else:
    print("We can't decide")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("May be we should take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, lets take the truck.")

else:
    print("Fine let's stay home then.")