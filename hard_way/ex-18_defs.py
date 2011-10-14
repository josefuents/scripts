# this one is like your script with "argv"
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this is just one arguemtn
def print_one(arg1):
    print "arg1: %r" % (arg1)

# this takes no arguments
def print_none():
    print "I do nothing!"


print_two('hola', 'adios')
print_two_again('hola', 'adios')
print_one('primero')
print_none()
