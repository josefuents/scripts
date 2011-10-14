#
#   Template for 15-110 Homework #7
#
#   Problem #1: 1.matchNovels.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):
#
#   15-110 section:

import os

def getWordCounts(listOfWords):
    count = {}
    for word in listOfWords:
        count[word] = 1 + count.get(word, 0)
    return count

def getWordFreqs(wordCounts):
    counts = wordCounts
    max_key = float(counts[max(counts.keys())])
    freq = {}
    for key, value in counts.iteritems():
        div = value / max_key
        freq[key] = div
    return freq
       
def getAllWords(wordFreqs1, wordFreqs2):
    allWords = []
    for key, value in wordFreqs1.iteritems():
        for key1, value1 in wordFreqs2.iteritems():
            if key not in allWords:
                allWords.append(str(key))
            elif key1 not in allWords:
                allWords.append(str(key1))
    return allWords

def getWordFreqsMatch(wordFreqs1, wordFreqs2):
    return 42 # YOU WRITE THIS FUNCTION!

def getImprovedWordFreqsMatch(wordFreqs1, wordFreqs2):
    # For now, just call the default wordFreqsMatch
    # BONUS/OPTIONAL:  See if you can do better!
    return getWordFreqsMatch(wordFreqs1, wordFreqs2)

########################################
### Test code
########################################

def testGetWordCounts():
    print "Testing getWordCounts()...",
    listOfWords = [ "dog", "cat", "ant", "cat", "gnu",
                    "cow", "dog", "cat" ]
    wordCounts = getWordCounts(listOfWords)
    assert(wordCounts["dog"] == 2)
    assert(wordCounts["cat"] == 3)
    assert(wordCounts["ant"] == 1)
    assert(wordCounts["gnu"] == 1)
    assert("mouse" not in wordCounts)
    print "Passed!"

def almostEqual(d1, d2):
    epsilon = 0.0000001
    return abs(d1 - d2) < epsilon

def testGetWordFreqs():
    print "Testing getWordFreqs()...",
    wordCounts = dict([("dog", 3), ("cat", 2), ("gnu", 5)])
    wordFreqs = getWordFreqs(wordCounts)
    assert(almostEqual(wordFreqs["dog"], 0.6))
    assert(almostEqual(wordFreqs["cat"], 0.4))
    assert(almostEqual(wordFreqs["gnu"], 1.0))
    assert("cow" not in wordFreqs)
    print "Passed!"

def testGetAllWords():
    print "Testing getAllWords()...",
    wordCounts1 = dict([("dog", 3), ("cat", 2), ("gnu", 5)])
    wordFreqs1 = getWordFreqs(wordCounts1)
    wordCounts2 = dict([("cat", 5), ("frog", 3), ("gnu", 7)])
    wordFreqs2 = getWordFreqs(wordCounts2)
    allWords = getAllWords(wordFreqs1, wordFreqs2)
    assert(sorted(allWords) == ["cat", "dog", "frog", "gnu"])
    print "Passed!"    

def testGetWordFreqsMatch():
    print "Testing getWordFreqsMatch()...",
    wordCounts1 = dict([("dog", 3), ("cat", 2), ("gnu", 5)])
    wordFreqs1 = getWordFreqs(wordCounts1)
    wordCounts2 = dict([("cat", 5), ("frog", 3), ("gnu", 7)])
    wordFreqs2 = getWordFreqs(wordCounts2)
    match = getWordFreqsMatch(wordFreqs1, wordFreqs2)
    assert(almostEqual(match, 0.390510333988))
    print "Passed!"    
    
def testAll():
    testGetWordCounts()
    testGetWordFreqs()
    testGetAllWords()
    testGetWordFreqsMatch()

testAll()

########################################
### Support code
########################################

################## You may ignore below this line #################

def getWords(line):
    # assume line ends in a newline
    words = [ ]
    word = ""
    for ch in line.lower():
        if ((ch == " ") or (ch == "\n")):
            if (len(word)>0):
                words.append(word)
                word = ""
        elif ((ch >= "a") and (ch <= "z")):
            word += ch
    return words

def readNovel(novelFile):
    # Return mainText in lowercase.
    # mainText starts + ends with "***..."
    words = [ ]
    inMainText = False
    with open(novelFile,"r") as f:
        for line in f:
            if (line.startswith("***")):
                if (inMainText == False):
                    inMainText = True
                else:
                    break
            elif (inMainText == True):
                words += getWords(line.lower())
    return words

def matchNovels(novel1, novel2):
    # 1 = perfect match; 0 = perfect mismatch
    words1 = readNovel(novel1)
    words2 = readNovel(novel2)
    wordCounts1 = getWordCounts(words1)
    wordCounts2 = getWordCounts(words2)
    wordFreqs1 = getWordFreqs(wordCounts1)
    wordFreqs2 = getWordFreqs(wordCounts2)
    return getImprovedWordFreqsMatch(wordFreqs1, wordFreqs2)

def matchAllNovels(novelsDir):
    if (not os.path.exists(novelsDir)):
        print "No such novelsDir:", novelsDir
        print "Did you download and unzip this to the same"
        print "folder where you placed Homework7?"
        return
    dirMatches = { }
    novels = os.listdir(novelsDir)
    for novel in novels:
        if (novel.endswith(".txt")):
            print "Checking", novel
            bestMatch = -1
            bestNovel = "no match!"
            for otherNovel in novels:
                if (otherNovel.endswith(".txt") and
                    (novel != otherNovel)):
                    # print "  Checking against", otherNovel
                    match = matchNovels(novelsDir + "/" + novel,
                                        novelsDir + "/" + otherNovel)
                    dirMatches[(novel, otherNovel)] = match
                    # print "  match =", match
                    if (match > bestMatch):
                        bestMatch = match
                        bestNovel = otherNovel
            # print "   bestMatch =", bestNovel
            dirMatches[novel] = bestNovel
    return dirMatches

def author(novel):
    # novel is a filename of form author-title-pg#.txt
    dashIndex = novel.index("-")
    return novel[0:dashIndex]

def reportMatches(matches):
    print "--------------------"
    print "Best matches:"
    for key in matches.keys():
        if (type(key) == type("")):
            novel = key
            print novel
            print "   ->", matches[novel]
            if (author(novel) != author(matches[novel])):
                print "   MISMATCH!"
    print "--------------------"
    print "Quality of metric:"
    qualityScore = 0
    matchCount = 0
    # 0 = worst, 1 = best
    for key in matches.keys():
        if (type(key) == type( () )):
            matchCount += 1
            (novel1, novel2) = key
            if (author(novel1) == author(novel2)):
                # same, so higher metric is better for novel2
                qualityScore += matches[key]
            else:
                # different, so lower metric is better for novel2
                qualityScore += (1 - matches[key])
    qualityScore = 1.0 * qualityScore / matchCount
    print "   ", qualityScore
    print "--------------------"

########################################
### If all tests pass, then
### run match algorithm on hw7-novels
########################################

matches = matchAllNovels("../hw7-novels")
reportMatches(matches)

"""
Expected output:
--------------------
Best matches:
twain-huck-finn-pg76.txt
   -> twain-tom-sawyer-pg74.txt
twain-tom-sawyer-pg74.txt
   -> twain-huck-finn-pg76.txt
alcott-little-men-pg2788.txt
   -> alcott-little-women-pg514.txt
james-the-american-pg177.txt
   -> james-daisy-miller-pg208.txt
alcott-little-women-pg514.txt
   -> alcott-little-men-pg2788.txt
james-daisy-miller-pg208.txt
   -> james-the-american-pg177.txt
--------------------
Quality of metric:
    0.412206618048
--------------------
"""

