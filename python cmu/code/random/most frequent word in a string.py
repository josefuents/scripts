
def str2list(string):
    ustring = string.upper() + " "
    nlist = []
    nstring = ""
    count = 0
    for i in ustring:
        for ustring in range(26):
            ch = chr(ord("A") + ustring)
            if i in ch:
                nstring = nstring + i   
        if i == " ":
            nlist. append(nstring)
            nstring = ""
    return nlist

def frequ(string):
    word_list = str2list(string)
    word_counter = {}
    print word_counter
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
            print word_counter[word], 'a'
        else:
            word_counter[word] = 1
            print word_counter[word], 's'

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    top_3 = popular_words[:3]
    print top_3


        

    
frequ('la la la la la la casa casa es es roja roja')
