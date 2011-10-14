#this script transforms upper case leeters into lower case letters and vise versa

ch0 = 'la casa Me Gusta'

for ch in ch0:
    if 'a' <= ch <= 'z':
        print chr(ord(ch)-ord('a') + ord('A')) + ' 1'
    elif 'A' <= ch <= 'Z':
        print chr(ord(ch)-ord('A') + ord('a')) + ' 2'
    else:
        print ch + ' 3'
