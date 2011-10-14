from sys import argv
from os.path import exists

script, filename, to_filename = argv

print "Copy file %r to file %r" % (filename, to_filename)

f = open(filename).read()

print "the " + filename + " is %r bytes long" % len(f)

print "Does the output file '" + to_filename + "' exist?: %r" % exists(to_filename)

o = open(to_filename, "w").write(f)

#oo = filename.close()
print "Done. The copy process is finished!"



