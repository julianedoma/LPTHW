from sys import argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:"
first = raw_input()
print "Your second variabe is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

# By giving fewer than three arguments to the script, it's giving an error message, since the code defines three variables
