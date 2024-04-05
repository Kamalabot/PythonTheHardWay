# This one is like the scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")
    #This function pulls in the args w/o argv import

def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")


def print_one(arg1):
    print(f"arg1:{arg1}")


def print_nen():
    print('I have nothing')


print_two('Zed','Shaw')

print_two_again('Kamal','raj')
print_one('one')
print_nen()