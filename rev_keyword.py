# some keywords checkings

# tr = False

# assert(tr)

def tryglo(low):
    global x 
    x = 'this is global'
    local = low
    print(f"this is functions printing {low}")


tryglo(60)

print(f"\v This is printing the variable inside fun {x}")