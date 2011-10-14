#example of a loop that prints a sequence between a 'while' condition

d = input("what is your deposti amount? :")
i = input("what interest do you wan tot get? :")
t = input("how much time do you wna to gove me the money? :")
year = 1
while(year <= t):
    d += ((d * i) / 100)
    print "you new balance after year", year, "is", d
    year += 1
print "your final balance is", d
    

