def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def mul(a,b):
    print(f"Multiplying {a} * {b}")
    return a * b

def sub(a,b):
    print(f"Subtacting {a} - {b}")
    return a - b

def div(a,b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions")

age = add(30,7)
height = sub(186,16)
weight = div(530,7)
iq = mul(50,2)

print("Printing the results")
print(f"Age achieved by adding is {age}")
print(f"Weight achieved by dividing is {weight}")
print(f"Height achieved by Subtracting is {height}")
print(f"IQ achieved by Multiplying is {iq}")

print("Here is a puzzle")

what = add(age,sub(height,mul(weight,div(iq,2))))

print("That becomes",what,"Can you do it by hand")