
def str2list(string):
    nlist = string.split()
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


        

    
frequ('la la la casa casa casa papa mam mama')
