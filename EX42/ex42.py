# Dog is-a object which inherits from the class Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat is-a object which inherits from class Animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has-a name
        self.name = name

#person is-a object
class Person(object):

    def __init__(self, name):
        #person has-a name
        self.name = name
        self.pet = None

#employee is-a object which inherits from class person
class Employee(Person):

    def __init__(self, name, salary):
        # ??
        super(Employee, self).__init__(name)
        # employee has-a salary
        self.salary = salary

# fish is-a object
class Fish(object):
    pass

# Salmon is-a object interiting from class fish
class Salmon(Fish):
    pass

# Hailbut is-a object interiting from class fish
class Hailbut(Fish):
    pass
# rover is-a dog
rover = Dog("Rover")
#satan is-a Cat
satan = Cat("Satan")
#mary is a Person
mary = Person("Mary")
#mary has-a attribute pet, the pet is satan
mary.pet = satan
#frank is-a employee with the parameters Frank (=name) and 120000 (0salary)
frank = Employee("Frank", 120000)
#frank has-a pet which is a rover
frank.pet = rover
#flipper is-a object of the class fish
flipper = Fish()
#crouse is an instance of the class Salmon
crouse = Salmon()
#harry is-a instance of the class Hailbut
harry = Hailbut()
