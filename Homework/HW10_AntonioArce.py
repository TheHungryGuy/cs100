# Problem 1
def initialLetterCount(wordList):
    wordDict = {}
    for x in wordList:
        if wordDict.get(x[0]) == None:
            wordDict[x[0]] = 1
        else: 
            count = wordDict.get(x[0]) + 1
            wordDict.update({x[0]: count}) 
    return wordDict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

# Problem 2
def initialLetters(wordList):
    wordDict = {}
    for x in wordList:
        if wordDict.get(x[0]) == None:
            wordDict[x[0]] = [x]
        else: 
            words = wordDict.get(x[0])
            if x not in words:
                words.append(x)
                wordDict.update({x[0]: words}) 
    return wordDict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton))

#Q3

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

def shareOneLetter(wordList):

    ourDict = {}
    for wordA in wordList: 
        if wordA not in ourDict:
            ourDict[wordA] = []
        for wordB in wordList:
            if wordPals(wordA,wordB) and wordB not in ourDict[wordA]:
                ourDict[wordA].append(wordB)

    print(ourDict)

    
def wordPals(wordA,wordB):
    for letterA in wordA:
        if letterA in wordB: return True
    return False

shareOneLetter(horton)