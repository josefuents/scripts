# transform a string into a list and a list back into a string


def splitAndJoin():
    n = raw_input("text to be converted to a list: ")
    l = list(n)
    print l
    s = ''.join(l)
    print s


splitAndJoin()


