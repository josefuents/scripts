def sumOddsFrom1ToN(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i
        print sum
    return sum
