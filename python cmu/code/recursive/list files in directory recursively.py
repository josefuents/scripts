import os
def listFiles(path):
    if (os.path.isdir(path) == False):
        # base case:  not a folder, but a file, so print its path
        print path
    else:
        # recursive case: it's a folder
        for filename in os.listdir(path):
            listFiles(path + "/" + filename)
