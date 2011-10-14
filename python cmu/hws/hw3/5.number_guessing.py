#
#   Template for 15-110 Homework #3
#
#   Problem #5: The number guessing game strikes again
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

# Implement the function numberGuessingGame(lowerBound, upperBound) after this line

low = input("what is your low number?: ")
high = input("what is your high number?: ")
x = (high + low) /2
print "is your number", x, "?"
choice = raw_input("hmm, lower... higher.. or am I right?: ")

while choice == "lower":
     x = (x + low) / 2
     print("is your number "),x, "?"
     choice = raw_input("hmm, lower... higher... or am I right?: ")

while choice == "higher":
     x = (x + high) / 2
     print("is your number "),x
     choice = raw_input("hmm, lower... higher... or am I right?: ")
print "your number is", x
     
     
         
               
         
