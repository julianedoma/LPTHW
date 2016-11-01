def fruitsalad(apple, peach, ananas, orange):
    print "I have %d apples." % apple
    print "Also, I have %d peaches and %d ananas." % (peach, ananas)
    print "Finally, I'll add %d oranges.\n" % (orange)

fruitsalad(3,2,1,4)

apple_count = 10
peach_count = 1
ananas_count = 2
orange_count = 4

fruitsalad(apple_count, peach_count, ananas_count, orange_count)

print "We want to do a fruitsalad for dessert. Let's see what we have."
print "How many apples do you have?",
apples = raw_input()
print "And how many peaches?",
peaches = raw_input()
