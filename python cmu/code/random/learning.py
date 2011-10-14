def wordCounts(wordList):
    counts = { }
    for word in wordList:
        counts[word] = 1 + counts.get(word, 0)
    return counts

wordList = [ "dog", "cat", "dog", "pig", "cow", "cat",
             "gnu", "dog", "ant", "gnu", "pig", "dog" ]


