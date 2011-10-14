def wordCount(s):
    count = 0
    space = True
    for ch in s:
        if (ch == " "):
            space = True
            print space
        elif (space == True):
            count += 1
            space = False
            print space
    return count
            


    

    
