#imports file
from sys import argv
#defines "what the commandline needs"to run the program, in this case the filename and the ex16
script, filename = argv
#string for filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#"space" for user to type in either ctrl-c or return
raw_input("?")
# show "opening the file..." & open file in write-mode
print "Opening the file..."
target = open(filename, 'w')
# show "truncating the file. Goodbye!" and empties file
print "Truncating the file. Goodbye!"
target.truncate()
#print belows line
print "Now I'm going to ask you for three lines."
# asks for 3 lines of input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#print belows line
print "I'm going to write these to the file."
#write inputs of user + uses new line for each input
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "And finally, we close it."
target.close()

#Study Drill 5: when opening file in "w"-mode, truncate() is not necessary since the file will be overwritten anyways
