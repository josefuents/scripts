
def getData():
    data = []
    name = ''
    while name != 'done':
        name = raw_input("enter name, or 'done' to finish: ")
        if name != "done":
            phoneNo = raw_input("enter " + name + "'s cell number: ")
            data.append([name, phoneNo])
    return data

def returnData():
    instruction = ''
    while instruction != 'retrive':
        make = getData()
        instruction = raw_input("wish to see your contacts, enter yes of no: ")
        if instruction == 'yes':
            print make
            for name, number in sorted(make):
                print "name: " + name + " number: " + number
                make = getData()
        if instruction == 'no':
            print 'Ok, the program is done'
            break


returnData()


    
