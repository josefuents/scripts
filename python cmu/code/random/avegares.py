
def averages():
    sum  = 0.
    count = 0
    num = input("enter a number: ")
    done = 'done'
    while num != 'done':
        sum += num
        count += 1
        num = input("enter a new number: ")
    print 'your sum is: ', sum, '(',sum,'/',count,')', 'and your average is: ', sum / count
    averages()

averages()

