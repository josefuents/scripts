
def cont():
    i = raw_input('continue? ')
    while True:
        if i == 'yes':
            print i
            i = raw_input('continue?? ')
        elif i == 'y':
            print i
            i = raw_input('continue?? ')

        else:
            print 'done'
            break
cont()
         
