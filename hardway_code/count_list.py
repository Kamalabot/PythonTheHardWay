the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This is first kind of for loop goes through the list

for number in the_count:
    print(f"The count is {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print("I got {i}")

elements = []

for i in range(0,6):
    print(f"Adding {i} to the list, actually appending")
    elements.append(i)

for i in elements:
    print(f"The element was {i}")