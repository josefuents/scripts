def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def divi(a,b):
    return a / b


age = add (23, 4)
height = sub(190, 10)
weight = mult(90, 2)
iq = divi(100,2)

print "Your age is %r,\n your height is %r,\n your weight is %r,\n and your IQ is %r" % (age, height, weight, iq)

what = add(age, sub(height, mult(weight, divi(iq, 2))))

print "what is equal to ", what, 
