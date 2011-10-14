import codecs 

sentence = codecs.open('a_a.txt', 'r', 'utf-8')
cognate = codecs.open('c_c.txt', 'r', 'utf-8')

cog_list = []
sent_list = " "

for cogs in cognate:
    cog_list.append(cogs.rstrip())    
    for sents in sentence:
        sent_list += sents.rstrip()
for cog_len in range(len(cog_list)):
    if cog_list[cog_len] not in sent_list:
        print cog_list[cog_len]
            

       	  
