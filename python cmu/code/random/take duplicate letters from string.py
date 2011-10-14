import string

def takeout(s):
    n = ''
    for i in s:
        if i not in string.ascii_letters:
            n += i
        elif i not in n:
            n += i
    print n
