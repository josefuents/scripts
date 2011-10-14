print "lets\'s practice everything\n You need to\ pa be able to print in\t @@@"


poem = """
\t the love
with magic
can make good stuff
yeah!!!!!"""

print "________________"
print poem
print "_________________"

five = 10 -2 +3 - 6
print "This should be five: %r" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "with a starting point of %r" % start_point

print "we'd have %r beans, %r jars, and %r crates." % (beans, jars, crates)

start_point = start_point / 10

print "we can also do it this way: "
print "we'd have %r beans, %r jars, and %r crates." % secret_formula(start_point)
