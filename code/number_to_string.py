def numToString(num):
    if num == 0: return 'zero'
    elif num <= -1: return 'nothing--number must be possitve!'
    elif num == 1: return 'one'
    elif num == 2: return 'two'
    elif num == 3: return 'three'
    elif num == 4: return 'four'
    elif num == 5: return 'five'
    elif num == 6: return 'six'
    elif num == 7: return 'seven'
    elif num == 8: return 'eight'
    elif num == 9: return 'nine'
    elif num == 10: return 'ten'
    elif num == 11: return 'eleven'
    elif num == 12: return 'twelve'
    elif num == 13: return 'thirdteen'
    elif num == 14: return 'fourteen'
    elif num == 15: return 'fifhteen'
    elif num == 16: return 'sixteen'
    elif num == 17: return 'seventeen'
    elif num == 18: return 'eighteen'
    elif num == 19: return 'nineteen'
    elif num <= 29: return 'twenty ' + numToString(num%10)
    elif num <= 39: return 'thirty ' + numToString(num%10)
    elif num <= 49: return 'fourty ' + numToString(num%10)
    elif num <= 59: return 'fifty ' + numToString(num%10)
    elif num <= 69: return 'sixty ' + numToString(num%10)
    elif num <= 79: return 'seventy ' + numToString(num%10)
    elif num <= 89: return 'eighty ' + numToString(num%10)
    elif num <= 99: return 'ninety ' + numToString(num%10)
    elif num >= 99: return 'this program runs untill the number 99'


while True:
    n = numToString(input('number: '))
    print 'the number is', n


