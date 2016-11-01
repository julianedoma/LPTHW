#importing files into the program, argv ="argument variable"; holds arguments

#upacking argv; assignes to variables
filename = raw_input ("> ")
#tells program to open certain file
txt = open(filename)
#prints out below's sentence including string of filename
print "Here's your file %r:" % filename
#tells program to print out the text the file is containing
print txt.read()
#tells program to print below's sentence
print "Type the filename again:"
#tells program that there will be 'anything' typed in, more than 0 letters
file_again = raw_input("> ")
#tells program to open textfile
txt_again = open(file_again)
#tells program to print out content of text file
print txt_again.read()
