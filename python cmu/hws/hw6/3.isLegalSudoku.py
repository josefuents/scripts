#
#   Template for 15-110 Homework #6
#
#   Problem #3: 3.isLegalSudoku.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

import copy

def areLegalValues(values):
    return False # replace with your code!

def isLegalRow(board, row):
    return False # replace with your code!

def isLegalCol(board, col):
    return False # replace with your code!

def isLegalBlock(board, block):
    return False # replace with your code!

def isLegalSudoku(board):
    return False # replace with your code!


################## You may ignore below this line #################

okBoard1 = [
 [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
 [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
 [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
 [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
 [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
 [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
 [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
 [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
 [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

okBoard2 = [
 [ 5, 3, 4, 6, 7, 8, 9, 1, 2 ],
 [ 6, 7, 2, 1, 9, 5, 3, 4, 8 ],
 [ 1, 9, 8, 3, 4, 2, 5, 6, 7 ],
 [ 8, 5, 9, 7, 6, 1, 4, 2, 3 ],
 [ 4, 2, 6, 8, 5, 3, 7, 9, 1 ],
 [ 7, 1, 3, 9, 2, 4, 8, 5, 6 ],
 [ 9, 6, 1, 5, 3, 7, 2, 8, 4 ],
 [ 2, 8, 7, 4, 1, 9, 6, 3, 5 ],
 [ 3, 4, 5, 2, 8, 6, 1, 7, 9 ]
]

badBoard1 = copy.deepcopy(okBoard1)
badBoard1[0][0] = 7

badBoard2 = copy.deepcopy(okBoard2)
badBoard2[8][8] = 8

print "Testing areLegalValues()...",
assert(areLegalValues([0, 1, 2, 3, 4, 5, 6, 7, 8]) == True)   # partial set
assert(areLegalValues([7, 3, 1, 5, 2, 9, 8, 4, 6]) == True)   # full set! 
assert(areLegalValues([0, 1, 2, 3, 4, 5, 6, 7, 0]) == True)   # duplicate blanks are ok 
assert(areLegalValues([1, 2, 3, 2, 4, 5, 6, 7, 9]) == False)  # duplicate values are not
assert(areLegalValues([10, 1, 2, 3, 4, 5, 6, 7, 8]) == False) # out of range
assert(areLegalValues([-1, 1, 2, 3, 4, 5, 6, 7, 8]) == False) # out of range
print "Passed!"

print "Testing isLegalRow()...",
assert(isLegalRow(okBoard1, 0) == True)
assert(isLegalRow(badBoard1, 0) == False)
print "Passed!"

print "Testing isLegalCol()...",
assert(isLegalCol(okBoard1, 0) == True)
assert(isLegalCol(badBoard1, 0) == False)
print "Passed!"

print "Testing isLegalBlock()...",
assert(isLegalBlock(okBoard2, 8) == True)
assert(isLegalBlock(badBoard2, 8) == False)
print "Passed!"

print "Testing isSudokuBoard()...",
assert(isLegalSudoku(okBoard1) == True)
assert(isLegalSudoku(badBoard1) == False)
assert(isLegalSudoku(okBoard2) == True)
assert(isLegalSudoku(badBoard2) == False)
print "Passed!"
