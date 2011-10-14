# to properly run this script you must include a file name

from sys import argv

script, filename = argv

t = open(filename)
print t.read()
w = raw_input(">")
w1 = open(w)
print w
print w1.read()
