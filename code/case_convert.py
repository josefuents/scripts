


def caseConvert():
    stChars = (list (raw_input("give me a sentence ")))
    print stChars
    for i in range(0, len(stChars)):
        if 'a' <= stChars[i] <= 'z':
             stChars[i] = chr(ord(stChars[i]) - ord('a') + ord('A'))
        elif 'A' <= stChars[i] <= 'Z':
            stChars[i] = chr(ord(stChars[i]) - ord('A') + ord('a'))
    print ''.join(stChars)

            


caseConvert()
