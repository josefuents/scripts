def Dues():
    nameAndDue = raw_input("enter name + amount, separated by a colon: ").split(',')
    dues = {}
    while nameAndDue != ['q']:
        dues[nameAndDue[0]] = dues.get(nameAndDue[0], 0.00) + eval(nameAndDue[1])
        nameAndDue = raw_input("enter name + amount, separated by a colon: ").split(',')
    for name in dues:
        print name, " had paid ", dues[name]


Dues()

