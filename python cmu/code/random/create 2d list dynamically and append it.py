def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

rows = 3
cols = 2
a = make2dList(rows, cols)
print "This IS ok.  At first:"
print "   a =", a

a[0][0] = 42
print "And now see what happens after a[0]=42"
print "   a =", a
