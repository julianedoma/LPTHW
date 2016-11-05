#defining variables
people = 30
cars = 40
trucks = 15

# if the amount of cars is greater than people print line below
if cars > people:
    print "We should take the cars."
#if amount of cars is less than people print "We should not take the cars" if the statement is not true print sentence below
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine let's stay home then."
