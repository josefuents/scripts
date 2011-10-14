def reverse(s):
    rev = ""
    for ch in s:
        rev = ch + rev
        print rev
    return rev
