def fib(n):
    if (n < 2):
        # Base case:  fib(0) and fib(1) are both 1
        return 1
    else:
        # Recursive case:  fib(n) = fib(n-1) + fib(n-2)
        return fib(n-1) + fib(n-2)

for n in range(10): print fib(n),
