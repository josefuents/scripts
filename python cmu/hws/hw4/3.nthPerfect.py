#
#   Template for 15-110 Homework #3
#
#   Problem #3: nthPerfect
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:


# Implement the helper function  sumOfProperFactors(n) after this line


# Implement the helper function  isPerfect(n) after this line


# Implement the function  nthPerfect(n) after this line



# These assertions are here for your benefit.  They are not exhaustive:
# the CA's will use more tests when grading your final submissions.
# Feel free to add/remove tests here, just be careful!

assert(sumOfProperFactors(-22) == 0)
assert(sumOfProperFactors(1) == 0)
assert(sumOfProperFactors(6) == 6)
assert(sumOfProperFactors(8) == 7)
       
print("Passed all tests for sumOfProperFactors!")

assert(isPerfect(-22) == False)
assert(isPerfect(5) == False)
assert(isPerfect(6) == True)
# We'll just comment this next one out for now...
#assert(isPerfect(2658455991569831744654692615953842176) == True) (eventually)

print("Passed all tests for isPerfect!")


assert(nthPerfect(0) == 6)
assert(nthPerfect(1) == 28)
assert(nthPerfect(2) == 496)
assert(nthPerfect(3) == 8128)
assert(nthPerfect(-22) == -1)

print("Passed all tests for nthPerfect!")
