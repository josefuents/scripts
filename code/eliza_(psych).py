import string

def getReply(line, words):
    if len(words) == 0 : return "You have to talk to me. "
    if line[-1] == "?" : return "What do you want to know? "
    if "mother" in words : return "Tell me more about your mother. "
    if "father" in words : return "Tell me more about your thaer. "
    if "brother" in words : return "Tell me more about your brother. "
    if "sister" in words : return "Tell me more about your sister. "
    if len(words) <= 2 : return "I did not understand. Can you be more explitic? "
    if words[0] == "i" and words[1] == "think" : return "Do you really think so? "
    if words[0] == "i" and words[1] == "want" : return "Why do you want so? "
    if words[0] == "i" and words[1] == "feel" : return "Why do you feel that way? "
    if words[0] == "yes" or words[0] == "no" : return "I see. Interesting. Tell me more. "    
    
    return "Tell me more. "    

name = raw_input('Hello. Welcome to therapy. What is you name? ')
print 'Type "quite" when you want to finish the therapy session'
line = raw_input('Well ' + name + ', what can I do for you today? ')

while line != "q":
    line = line.lower()
    reply = getReply(line, line.split())
    line = raw_input(reply)



