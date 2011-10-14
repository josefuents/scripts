#
#   Template for 15-110 Homework #6
#
#   Problem #2: 2.mastermindScore.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

import copy

def mastermindScore(code, guess):
    return None  # replace with your solution



################## You may ignore below this line #################

print "Testing mastermindScore()...",
assert(mastermindScore([3,4,5,6], [3,3,4,6]) == [2,1])
assert(mastermindScore([3,4,5,6], [1,2,3,4]) == [0,2])
assert(mastermindScore([3,4,5,6], [3,4,3,4]) == [2,0])
assert(mastermindScore([3,4,5,6], [1,1,1,1]) == [0,0])
assert(mastermindScore([3,4,5,6], [3,3,3,3]) == [1,0])
assert(mastermindScore([3,4,5,6], [2,3,3,3]) == [0,1])
print "Passed!"
