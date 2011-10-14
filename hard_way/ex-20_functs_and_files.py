from sys import argv


scrip, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "first: read file"

print_all(current_file)

print "now lets rewind--like a tape"

rewind(current_file)

print "print 3 lines"

current_l = 1
print_a_line(current_l, current_file)

current_l += 1
print_a_line(current_l, current_file)

current_l += 1
print_a_line(current_l, current_file)

