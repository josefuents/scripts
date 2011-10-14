def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True

# And take it for a spin
for n in range(19):
    if isPrime(n):
        print n,


def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in range(2,maxFactor+1):
        if (n % factor == 0):
            return False
    return True

# Verify these are the same
for n in range(1000):
    if (isPrime(n) != fasterIsPrime(n)): print n
    assert(isPrime(n) == fasterIsPrime(n))
print "They seem to work the same!"
