def NumberLetter():
    r = raw_input("enter date en in numbers, e.x. 03.03.2003: ")
    print r
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    day = ['First', 'Second', 'Third', 'Forth', 'Fifth', 'Six', 'Seventh', 'Eighth', 'Nineth', 'Tenth']
    year = ['two thousand and eleven']
    mon, da, yea = r.split('.')
    print mon
    
    print month[eval(mon) -1 ] + ' ' + day[eval(da) - 1 ] + ', ' 

NumberLetter()


