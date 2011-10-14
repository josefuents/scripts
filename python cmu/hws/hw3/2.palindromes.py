#
#   Template for 15-110 Homework #3
#
#   Problem #2: Palindromes
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

# Implement the function isPalindrome(word) after this line

def isPal(w):
    return w[::-1] == w
    
   



# DO NOT CHANGE THE CODE BELOW THIS LINE

assert(isPal("kayak") == True)
assert(isPal("palindrome") == False)
assert(isPal("yay yay") == True)
assert(isPal("abba") == True)
assert(isPal("abca") == False)
assert(isPal("x") == True)
assert(isPal("") == True)

print("Passed all tests!")

