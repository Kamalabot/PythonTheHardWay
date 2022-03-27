from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_aline(line_index,f): #It is index,
    #print(line_index,f.readline(line_index))
    print(line_index,f.readline(),end=' ')

current_file = open(input_file)

print("First lets print the whole file")
print_all(current_file)

print("Now Rewind")
rewind(current_file)

print('Lets print line by line')

current_l = 5
print_aline(current_l,current_file)

current_l = current_l + 1
print_aline(current_l, current_file)

current_l = current_l + 1
print_aline(current_l,current_file)