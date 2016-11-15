#define class parent
class Parent(object):
#define fuction override, which prints "parent override" and overrides other classes
    def override(self):
        print "PARENT override()"
#define function implicit, which makes child classes inherit instances of the parent class
    def implicit(self):
        print "PARENT implicipt()"
#define function altered which makes changes on the parent class
    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def atlered(self):
        print "CHILD BEFORE PARENT, altered()"
        super(Child, self).altered()
        print "CHILD AFTER PARENT, atlered()"

dad = Parent()
son = Child()
#PARENT implicit
dad.implicit()
#PARENT implilcit
son.implicit()
#Parent override
dad.override()
#child override
son.override()
#parent altered
dad.altered()
#child before parent altered
#parent altered
#child after parent atlered
son.altered()
