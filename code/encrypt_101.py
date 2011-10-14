
def Encrypt():
    r = raw_input("message: ")
    message = ""
    for l in r:
        message += " " + str(ord(l))
    print 'your message has been encrypted as: ', message
    Decrypt()

def Decrypt():
    r = raw_input("message: ")
    s = r.split()
    message = ""
    for n in s:
        message += chr(eval(n))
    print 'your message has been decrypted as: ', message

Encrypt()

