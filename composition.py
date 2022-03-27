class Other(object):

    def override(self):
        print("Other Override()")

    def implicit(self):
        print("Other implicit()")

    def altered(self):
        print("Other altered()")

class Child(object): #No inheritance, that is is-a

    def __init__(self):
        self.other = Other() 
        #We make one of objects of Other and assign it to child attribute 

    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("Child Override()")

    def altered(self):
        print("Child, before Other ALtered")
        self.other.altered()
        print("Child after Other ALtered")

son = Child()
son.implicit()
son.override()
son.altered()

print('\n')
print('Other object parameter')
alien = Other()
alien.altered()
alien.implicit()
alien.override()