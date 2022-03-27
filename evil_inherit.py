class Parent():
    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

print("Direct inherited printing")
dad.implicit()
son.implicit()

class Parent():
    def override(self):
        print("Parent override()")

class Child(Parent):
    def override(self):
        print("Child override()")

print("\n")
print("Inherit override print")
dad = Parent()
son = Child()

dad.override()
son.override()

class Parent():
    def altered(self):
        print("Parent altered()")
    def power(self):
        print("Special parent Power")
class Child(Parent):
    def altered_child(self):
        print("Child Before parent altered()")
        super(Child,self).altered()
        print("Child after parent altered()")

print("\n")
print("Inherit altered print")
dad = Parent()
son = Child()

dad.altered()
son.altered()

#let try multiple inheritance, but throws cycling error

#class Husband(Parent,Child):
 #   pass #nothing given

tubby = Husband()
tubby.power()