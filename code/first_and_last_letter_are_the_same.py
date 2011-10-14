

def FirstLast():
    r = raw_input("enter words or a sentence: ")
    if len(r) <= 1: print r, True
    elif r[0] != r[-1]: print r, False, 'a'
    elif r[0] == r[-1] : print r, True, 'b'

FirstLast()



