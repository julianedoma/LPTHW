from sys import argv

script, filename = argv

txt = open(filename, "r")
print txt.readline()
