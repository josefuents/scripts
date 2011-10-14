#   Template for 15-110 Homework #6
#
#   Problem 4: 4.mysteryCode1.py
#
#
#   SOLVED BY (NAME & ANDREW ID):
#
#   15-110 section:
#

# Note: you must first replace the mastermindScore function (and any related helper functions)
# with your own solution!

import copy
import random

def mastermindScore(code, guess):
	raise Exception, "You must replace mastermindScore with your implementation!"

def playMastermind():
    codeLength = 4
    colors = 6
    print "\nMastermind!"
    print "code length is", codeLength
    print "colors are numbers from 1 to", colors
    while True:
        playMastermindRound(codeLength, colors)
        if (playAgain() == False):
            break
    print "Goodbye!"

def getGuess(guesses, scores):
    print "---------------"
    if (len(guesses) > 0):
        print "Guesses: "
        for i in range(len(guesses)):
            print "  Guess", (i+1), ":",
            print mystery1A(guesses[i]), "->",
            printScore(scores[i])
        print "---------------"
    guess = None
    while (guess == None):
        guess = mystery1B(raw_input("Next guess (as a 4-digit number, like 1234): "))
    return guess

def mystery1A(guess):
    string = ""
    for n in guess:
        string += chr(ord("0") + n)
    return string

def mystery1B(string):
    if (len(string) != 4):
        print "Guesses must be exactly 4 digits!"
        return None
    guess = [ ]
    for ch in string:
        if ((ch < "0") or (ch > "9")):
            print "Guesses must only contain digits!"
            return None
        guess += [ ord(ch) - ord("0") ]
    return guess

def mystery1C(length, colors):
    code = [ ]
    for i in range(length):
        code.append(random.randint(1,colors))
    return code

def printScore(score):
    print score[0], "exact and",
    print score[1], "partial"

def playMastermindRound(codeLength, colors):
    code = mystery1C(codeLength, colors)
    guesses = [ ]
    scores = [ ]
    turns = 0
    while True:
        print "\n**********"
        print "Debugging Hint:  code is:", code
        guess = getGuess(guesses, scores)
        if (guess in guesses):
            print "You already guessed that, silly!"
        score = mastermindScore(code, guess)
        print "You scored",
        printScore(score)
        guesses.append(guess)
        scores.append(score)
        turns += 1
        if (score[0] == len(code)):
            print "You got it in", turns, "turns!!!!"
            return

def playAgain():
    while True:
        response = raw_input("\nPlay again? [y]es or [n]o: ")
        if (response.startswith("y")):
            return True
        elif (response.startswith("n")):
            return False
        else:
            print "I don't understand.  Please try again."

playMastermind()