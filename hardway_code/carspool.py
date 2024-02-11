car = 100 # Assigning 100 to car
space_in_car = 4 # Assigning 4 to space avlbl
drivers = 30 # Assigning drivers avlbl
passengers = 90 # Assigning today's passenger
cars_not_driven = car - drivers # calculate
cars_driven = drivers # Logic-assign drivers to cars driven
carpool_capacity = cars_driven*space_in_car
#calculate carpool capacity
average_passenger_per_car = passengers/ cars_driven
#calculate the average passenger per car
#Printing of the values start from here..
print('There are',car,'cars available')
print('There are only',drivers,'drivers available')
print('There will be',cars_not_driven,'empty cars today')
print('We can transport',carpool_capacity,'people today')
print('We have',passengers,'to carpool today')
print('we need to put about',average_passenger_per_car, 
'in each car')