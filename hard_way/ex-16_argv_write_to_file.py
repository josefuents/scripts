from sys import argv

script, filename = argv

print "are you sure you want to delete the content of the file?"

print "Opening the file..."
f = open(filename, "w")

print "File's content deleted!"

print "Now enter 3 new lines"

l1 = raw_input(">")
l2 = raw_input(">")
l3 = raw_input(">")

f.write(l1 + "\n" + l2 + "\n" + l3 + "\n")

f.close()
print "We are done. These are your lines"
f1 = open(filename, "r")

for l in f1:
    print l, 



