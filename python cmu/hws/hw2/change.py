#
#   Template for 15-110 Homework #2
#
#   Problem #3: change.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:
#


def changes():
    cents = input("how many cents do you have today: ")
    quarter = cents / 25    
    rest = cents % 25
    dime = rest / 10
    take = cents - ((25 * quarter) + (10 * dime))
    nickle = take / 5
    cent = take % 5
    
    print("thank you for your input!")
    print("your total number of cents is: " + str(cents))
    print("number of quarters needed: " + str(quarter))
    print("number of dimes needed: " + str(dime))
    print("number of nickles needed: " + str(nickle))
    print("number of cents needed: " + str(cent))
