#
#   Template for 15-110 Homework #6
#
#   Problem #1: 1.mostFrequentWord.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

import copy

def mostFrequentWord(text):
    return "python"  # replace with your solution


################## You may ignore below this line #################

print "Testing mostFrequentWord()...",

assert(mostFrequentWord("") == None)
assert(mostFrequentWord("This is a test!") == "A")
joke = """
You can say any foolish thing to a dog,
and the dog will give you this look that says,
"My God, you are right! I never would've thought of that!"
Dave Barry
"""
assert(mostFrequentWord(joke) == "YOU")
assert(mostFrequentWord("wow gosh wow!!! gosh!!!! wow.  No way.  Yes way.  Way!  gosh.") == "GOSH")

print "Passed!"
