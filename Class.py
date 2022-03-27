##Animal is-a object 

class Animal(object):
    pass #Necessary to ensure class is not empty

#Dog is-a Animal that has-a __init__ that takes name params 
class Dog(Animal):
    def __init__(self,name):
        ##Initialising the name attribute
        self.name = name

#Cat is-a Animal, that has-a __init__ that takes name params
class Cat(Animal):
    def __init__(self,name):
        ##Initialising the name attribute
        self.name = name

#Person is-a object
class Person(object):
    def __init__(self,name):
        ##Intialising the name attribute
        self.name = name
        self.pet = None

##Employee is-a Person
class Employee(Person):
    def __init__(self,name,salary):
        ##Employee inheriting the name from Person
        super(Employee,self).__init__(name)
        ##Intialising Employee own attribute salary
        self.salary = salary
##Fish is-a object
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("rover")

## satan is-a cat
satan = Cat('satan')

## mary is-a Person
mary = Person("Mary")

## mary has-a attribute pet to which satan is set
mary.pet = satan

## frand is-a Employee which inherits Person
frank = Employee("Frank",12900)

## mary has-a attribute pet to which satan is set
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

##Crouse is-a Salmon which inherits Fish
crouse = Salmon()

##harry is-a Halibut which inherits Fish
harry = Halibut()
