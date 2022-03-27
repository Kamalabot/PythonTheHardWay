formatter = "{} {} {} {}"
#We are calling the string's formatting function
print(formatter.format(1,2,'\\4','az'))
#To that function we are passing the variables
print(formatter.format('\tw','\ntor','a.6',8))
#tab on the command line is 8 spaces!!!
print(formatter.format(True,True,False,True))
print(formatter.format(formatter,formatter,formatter,formatter)) 
print(formatter.format(
    "Try your",
    "Own text here.",
    "Live fire free",
    "Burns high heel-"
))

#We can do this way too
print(f"The new way is {2},{3},{6},{'8'}")
#Either way the 8 will be string, with or without quotes