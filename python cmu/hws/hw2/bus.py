#
#   Template for 15-110 Homework #2
#
#   Problem #5: bus.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:
#


#implement the function nearestBusStop (street) after this line

def bs(street):
    return(((street + 3) /8) * 8)



8
16
24
32
40
48
56
72
80


# DO NOT CHANGE THE CODE BELOW THIS LINE

assert(bs(11) == 8)
assert(bs(13) == 16)
assert(bs(12) == 8)
assert(bs(24) == 24)
assert(bs(129) == 128)

print("Passed all tests!")
