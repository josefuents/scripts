#   Template for 15-110 Homework #7
#
#   Problem #2: 2.sokoban.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:


"""
Your tasks:
0. Run the program, play the game, get a sense of what the code
   is trying to do.  Then study the code to see HOW it is doing it.

1. Answer the following questions (place your answers right here!):
a) What does it mean if grid[row][col] is "."?  "p"?
b) What does it mean if isGoal[row][col] is True?
c) What does the findPlayer function do?
d) Briefly explain why the following moves the player to the left:
        movePlayer(canvas, 0, -1)

2. As the game is written, when the player moves over a goal, you
   cannot tell that a goal is there (only the player is drawn).
   Change the code so that the background turns blue rather than
   gray when the player moves over a goal (so that there is a clear
   visual way to see that the player is over a goal rather than a non-goal cell).
   Note: you may want to change the parameters of at least one function
   to help achieve this task.

3. Add an "undo" function, where pressing "u" should undo the last
   move.  To do this, first add an "undoList" to the canvas.data.
   This is a list of each move that is attempted.  When the user presses undo,
   we don't actually undo the last move.  Instead, remove the last move from
   the undoList, and then call init() to start the game over, and
   then call movePlayer once for each move in undoList.
   
"""

from Tkinter import *

def findPlayer(canvas):
    grid = canvas.data["grid"]
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if (grid[row][col] == "p"):
                return (row, col)
    return None # should never happen!

def movePlayer(canvas, drow, dcol):
    grid = canvas.data["grid"]
    isGoal = canvas.data["isGoal"]
    rows = len(grid)
    cols = len(grid[0])
    (row0,col0) = findPlayer(canvas)
    (row1,col1) = (row0+drow, col0+dcol)
    target1 = grid[row1][col1]
    if (target1 == "w"):
        print "cannot move through a wall!"
    elif (target1 == "-"):
        # move to a blank
        grid[row0][col0] = "-"
        grid[row1][col1] = "p"
    elif (target1 == "b"):
        (row2,col2) = (row1+drow, col1+dcol)
        target2 = grid[row2][col2]
        if (target2 == "-"):
            grid[row0][col0] = "-"
            grid[row1][col1] = "p"
            grid[row2][col2] = "b"
        else:
            print "cannot push ball through an obstacle!"
    else:
        print "unknown target:", target1 # should never happen

def keyPressed(event):
    canvas = event.widget.canvas
    if (event.keysym == "Left"):
        movePlayer(canvas, 0, -1)
    elif (event.keysym == "Right"):
        movePlayer(canvas, 0, +1)
    elif (event.keysym == "Up"):
        movePlayer(canvas, -1, 0)
    elif (event.keysym == "Down"):
        movePlayer(canvas, +1, 0)
    elif (event.char.lower() == "r"):
        init(canvas)
    redrawAll(canvas)

def drawCellBackground(canvas, piece, left, top, right, bottom):
    if (piece == "."):
        color = "black" # outside
    elif (piece == "w"):
        color = "white" # wall
    else:
        color = "darkGray" # inside
    canvas.create_rectangle(left, top, right, bottom, fill=color)

def drawCellForeground(canvas, piece, isGoal, left, top, right, bottom):
    color = None
    if (piece == "p"):
        color = "green" # player
    elif (piece == "b"):
        color = "brown" # ball out of goal
        if (isGoal == True):
            color = "gold" # ball in goal                    
    elif (isGoal == True):
        color = "blue" # empty goal
    if (color != None):
        canvas.create_oval(left, top, right, bottom, fill=color)

def drawCell(canvas, row, col):
    grid = canvas.data["grid"]
    isGoal = canvas.data["isGoal"]
    rows = len(grid)
    cols = len(grid[0])
    cellSize = 30
    piece = grid[row][col]
    left = cellSize * col
    right = left + cellSize
    top = cellSize * row
    bottom = top + cellSize
    drawCellBackground(canvas, piece, left, top, right, bottom)
    drawCellForeground(canvas, piece, isGoal[row][col], left, top, right, bottom)

def redrawAll(canvas):
    canvas.delete(ALL)
    # draw the grid, cell by cell
    grid = canvas.data["grid"]
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, row, col)

def getStartGrid():
    # w=wall, p=player, b=ball, g=goal, -=blank, .=background
    grid = [["w","w","w","w","w",".",".",".","."],
            ["w","p","-","-","w",".",".",".","."],
            ["w","-","b","b","w",".","w","w","w"],
            ["w","-","b","-","w",".","w","g","w"],
            ["w","w","w","-","w","w","w","g","w"],
            [".","w","w","-","-","-","-","g","w"],
            [".","w","-","-","-","w","-","-","w"],
            [".","w","-","-","-","w","w","w","w"],
            [".","w","w","w","w","w",".",".","."]
            ]
    return grid

def getIsGoalGrid(grid):
    # make the isGoal grid
    rows = len(grid)
    cols = len(grid[0])
    isGoal = [ ]
    for row in range(rows): isGoal += [[False] * cols]
    # load isGoal grid and remove g's from the main grid
    for row in range(rows):
        for col in range(cols):
            if (grid[row][col] == "g"):
                grid[row][col] = "-"
                isGoal[row][col] = True
    return isGoal

def init(canvas):
    # make the main grid and the isGoal grid
    grid = getStartGrid()
    isGoal = getIsGoalGrid(grid)
    # and store these in canvas.data
    canvas.data["grid"] = grid
    canvas.data["isGoal"] = isGoal
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=270, height=270)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    #root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    #timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
