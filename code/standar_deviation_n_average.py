# difine standard derivation from a list of numbers.

import math

def std(data, ave):
    diffs = 0.0
    for x in data:
        xdiffs = x - ave
        diffs = diffs + xdiffs * xdiffs
    if len(data) == 0: return 0
    else: return math.sqrt(diffs / len(data))


def average(data):
    sum = 0.
    for x in data:
        sum = sum + x
    if len(data) == 0: return 0
    else: return sum / len(data)

def main():
    print "enter values to be analyzed, use -1 to end list"
    data = []
    num = input("enter yout number: ")
    while num != -1:
        data.append(num)
        print data
        num = input("enter your number: ")
    ave = average(data)
    print "the numbers are", data,
    print "average of data values is ", ave
    stdd = std(data, ave)
    print "standard deviation is", stdd



main()

