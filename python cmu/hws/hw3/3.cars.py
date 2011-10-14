#
#   Template for 15-110 Homework #3
#
#   Problem #3: Let's buy a new car
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

# Implement the function compareCars(years) after this line

def cc(years):
    #gass cost per year
    agass = (12000 / 25) * 2.7
    bgass = (12000 / 33) * 2.7
    #maintain fix
    amain = (300 * years) + (45 * years)
    bmain = (300 * years) + (30 * years)
    #anual ex
    aex = agass + amain
    bex = bgass + bmain

    count = ""
    while(len(count) < years):
        count += str(len(count))
        finala = (int(len(count)) * aex) + 15000
        print "Anual cost of car A will be: $", finala, "in year", str(len(count))
    countb = ""
    while(len(countb) < years):
        countb += str(len(countb))
        finalb = (int(len(countb)) * bex) + 18000
        print "Anual cost of car B will be: $", finalb, "in year", str(len(countb))
