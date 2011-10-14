def mysteryA(s1, s2):
    for i in range(min(len(s1), len(s2))):
        print range(min(len(s1), len(s2)))
        print i
        if (s1[i] != s2[len(s2)-1-i]):
            print i
            print s1[i]
            print s2[len(s2)-1-i]
            return False
    return len(s1) == len(s2)
