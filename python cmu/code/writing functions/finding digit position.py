#return one's digit
def onesDigit(x):
    return (abs(x) % 10)

def testOnesDigit():
    print "Testing onesDigit... ",
    assert(onesDigit(123) == 3)
    assert(onesDigit(7890) == 0)
    assert(onesDigit(6) == 6)
    assert(onesDigit(-54) == 4)
    print "Passed all tests!"

#return tens digits

def tensDigit(x):
    return onesDigit( x / 10)

def testTensDigit():
    print "Testing tensDigit... ",
    assert(tensDigit(1) == 0)
    assert(tensDigit(23) == 2)
    assert(tensDigit(456) == 5)
    assert(tensDigit(-7890) == 9)
    print "Passed all tests!"


def hunDigitx(x):
    return (onesDigit(tensDigit(x / 10)))
