# Instructions:
# run program in the desired directory.
import os

Directory = raw_input('what is the directory you want to use: ') 
File = raw_input('what is the name of the file you wish to delete: ')

def listFiles(path): # 'path' is the main directory used in the function--comes from input 'Directory'
    if (os.path.isdir(path) == False): # base case: 'path' not a folder and there are no files--do nothing
        pass         
    else:
        for filename in os.listdir(path): 
            listFiles(path + "/" + filename) # recursive case: it's a folder--remove file
            if filename != File:
                print File + ' not found in ' + path 
            elif filename == File:
                r = raw_input('are you sure you want to delete the file "' +  File + '"?\nlocated in ' + path + '/' + File + '\n' 'enter Y or n:' )
                if r == 'Y':
                    os.remove(path + "/" + File)
                    print 'the file ' + File + ' has been deleted!'
                else:
                    print "no file will be deleted."

listFiles(Directory) # target directory

