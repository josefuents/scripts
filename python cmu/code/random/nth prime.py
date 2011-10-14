def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isPrime(guess)):
            found += 1
    return guess

# and let's see a list of the primes
for n in range(10):
    print n, nthPrime(n)
