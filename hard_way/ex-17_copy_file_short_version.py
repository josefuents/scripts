from sys import argv
from os.path import exists

script, filename, to_filename = argv

f = open(to_filename, 'w').write(open(filename, 'r').read())
print "Done"


