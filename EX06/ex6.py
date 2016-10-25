#defining x with string inside
x = "There are %d types of people." % 10 #string put inside
# defining binary which is string element
binary = "binary"
# defining don't which is string element
do_not = "don't"
# defining variable y containing two strings
y = "Those who know %s and those who %s." % (binary, do_not)
#string put inside

# print variable x
print x
# print variable y
print y

# print statement containing string
print "I said %r." % x #string put inside
# print statement containing string
print "I also said: '%s'." % y #string put inside

# defining variable hilarious as 'false'
hilarious = False
# defining variable joke_evaluation containing string
joke_evaluation = "Isn't that joke so funny?! %r" #string put inside

# print combination of variables above
print joke_evaluation % hilarious
# defining variable w
w = "This is the left side of ..."
# defining variable e
e = "a string with a right side."

# print both variable above combined with + which adds both variable togehter and makes it longer
print w + e
