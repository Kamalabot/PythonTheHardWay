from sys import argv
script, first, second, third = argv

print("The script is calle:",script)
print("Your First variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)

print("Gimme 1 more arguments as input",end=' ')
arg1 = input('arg1:')
print('Gimme 2 more arg with comma seperate')
arg2 = input("arg2")

print(arg1, arg2)