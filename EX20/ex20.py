#importing variables
from sys import argv
#unpack imported variables, define input_file as variable
script, input_file = argv
#functionname print_all, argument: f, function tells program to read f
def print_all(f):
    print f.read()
#functionname: rewind, argument: f, tells to go to the beginning of the document
def rewind(f):
    f.seek(0)
#functionname: print_a_line;arguments: line_count, f;
def print_a_line(line_count, f):
    #tells program to read the first line of document
    print line_count, f.readline()
#defines current_file to open the input_file
current_file = open(input_file)
#print sentence + new line
print "First let's print the whole file: \n",
#read the input_file
print_all(current_file)
#print sentence
print "Now let's rewind, kind of like a tape."
#go to beginning of input_file
rewind(current_file)
#print sentence
print "Let's print three lines:"
#defines current_line as 1

#print first line of document with 1 (cause of "current line")

#again print line of document 1+1 =2
current_line = current_line =+ 1
print_a_line(current_line, current_file)
