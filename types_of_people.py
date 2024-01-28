types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"

do_not = "don't"

y = f"Those who know {binary} and who {do_not}"

print(x)
print()

print(f"I said: {x}")
# Seems to be taking the variable y in different way
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "Isn't that joke so funn? {}"
# Yeah, I get the joke...
print(joke_evaluation.format(hilarious))

print("Writing differently:Joke eval {}".format(hilarious))
w = "This is the left side of ..."
v = "a string with a right side"

print(w + v)
