#   Template for 15-110 Homework #6
#
#   Problem 4: 4.mysteryCode2.py
#
#
#   SOLVED BY (NAME & ANDREW ID):
#
#   15-110 section:
#

# Note: you must first replace the isLegalSudoku function (and any related helper functions)
# with your own solution!

def isLegalSudoku(board):
	raise Exception, "You must replace isLegalSudoku with your implementation!"

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

def mystery2A():
    print "     ",
    for col in range(9):
        print "col-" + chr(ord("A") + col),
    print
    
def printBoard(board):
    print
    mystery2A()
    for row in range(9):
        print "row-" + str(row+1),
        for col in range(9):
            print " ", str(board[row][col])," ",
        print "row-" + str(row+1)
    mystery2A()

def getMove():
    # move is list of 3 values: [ row, col, value ]
    # value of 0 means clear
    while True:
        response = raw_input("Enter move (or 'h' for help): ")
        if (response == "h"):
            print "Examples of legal moves:"
            print "   9 in B3"
            print "   clear A4"
            print "-----------"
        else:
            try:
                text = response.split()
                cell = text[-1]  # B3, A4, etc
                col = ord(cell[0]) - ord("A")
                row = ord(cell[1]) - ord("0") - 1
                if (text[0] == "clear"):
                    value = 0
                else:
                    value = int(text[0])
                if ((row < 0) or (row >= 9) or (col < 0) or (col >= 9)):
                    print "row and column must be between 1 and 9"
                elif ((value < 0) or (value > 9)):
                    # a little hacky -- what if the user enters value of 0?
                    print "value must be between 1 and 9"
                else:
                    return [ row, col, value ]
            except:
                print "Error.  Please try again."

def doMove(move, board):
    # move is list of 3 values: [ row, col, value ]
    # value of 0 means clear
    row = move[0]
    col = move[1]
    value = move[2]
    board[row][col] = value

def undoMove(move, board):
    # move is list of 3 values: [ row, col, value ]
    # value of 0 means clear
    row = move[0]
    col = move[1]
    value = move[2]
    board[row][col] = 0

def mystery2B(board):
    for row in range(9):
        for col in range(9):
            if (board[row][col] == 0):
                return False
    return True

def playSudoku(board):
    assert(isLegalSudoku(board))
    while (not mystery2B(board)):
        printBoard(board)
        move = getMove()
        doMove(move, board)
        if (isLegalSudoku(board) == False):
            print "Illegal move!"
            undoMove(move, board)
    print "Goodbye!"

playSudoku(okBoard1)
