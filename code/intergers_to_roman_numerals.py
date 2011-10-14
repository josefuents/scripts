
def romanDigit(n, onechar, fivechar, tenchar):
    if n == 0: return ''
    elif n == 1: return onechar
    elif n == 2: return onechar + onechar
    elif n == 3: return onechar + onechar + onechar
    elif n == 4: return onechar + fivechar
    elif n == 5: return fivechar
    elif n == 6: return fivechar + onechar
    elif n == 7: return fivechar + onechar + onechar
    elif n == 8: return fivechar + onechar + onechar + onechar
    elif n == 9: return onechar + tenchar
    else: print 'the number is out of range', n

def romanNumber(n):
    print (romanDigit((n/100) % 10, 'C', 'D', 'M') + 
    romanDigit((n/10) % 10, 'X','L','C') + 
    romanDigit(n%10, 'I', 'V', 'X'))

romanNumber(8)




