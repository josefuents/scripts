#this code creates a counter from 0 (s = "")
#to what ever 'x' interger you want

s = ""
while (len(s) < 5):
    s += str(len(s))
    print int(len(s))

