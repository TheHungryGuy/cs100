#Antonio Arce
#Antonio Ferreira

#exercise 4
'''write a function vowelStats() that takes a stirng
parameter: text containing words and white spaces
The function returns a list of containing the number
of vowels in each word in text.
For example,
if text is "Apple banana Orange Kiwi"
the function will return [2,3,3,2]
Grading scale:
10 pts if solved using a while loop
8 pts if solves using a for-loop
'''
def vowelStats(String):
    vowelList = String.split()
    wordPos = 0
    vowelNum = []
    while wordPos < len(vowelList):
        vowelNum.append(checkVowels(vowelList[wordPos]))
        wordPos+=1
    return vowelNum
    
def checkVowels(word):
    tempList = list(word)
    vowels="aeiouAEIOU"
    charPos=0
    count=0
    while charPos<len(tempList):
        if tempList[charPos] in vowels:
           count+=1 
        charPos+=1
    return count

text="Apple banana Orange Kiwi"
print(vowelStats(text))
