'''create a dictionary with the followoing information(students names
and their scores):
Jack    85
Jill    92
John    87


#1 iterate over the scores and print each one on a seprate line

#2 iterate over the keys, check the score for each one of those keys,
if it's greater than 90
print it
'''
d = {"Jack":85\
    ,"Jill":92\
    ,"John":87}

for score in d.values():
    print(score)

for student in d:
    if d[student] > 90:
        print(student)


'''Proplem 1. 
write a function wordFrequency() that takes 1 parameter,
1. text, a string containing words and white spaces
The function returns a dictionary of key:value pairs
where the key is a word in text and the value is the
number of times the word appears in text.
For example:
if text = "it is what it is", the function returns
("it":2, "is":2,"what":1)
'''
def wordFrequency(text):
    wordDict = {}
    words = text.split()
    for word in words:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    
    return wordDict
text = "it is what it is"
print(wordFrequency(text))

'''Problem2. write a function lengthFrequency() that takes 1 parameter:
1. text, a string containing words and white spaces.
The function returns a dictionary of key:value pairs, where the key is
the length of a word and the value is the number of words in the length.
For example:
if text = "it is what it is is is" the function returns
{2: 6, 4: 1}      #this means there are six words of length 2, and 1
word of length 4
'''

def lengthFrequency(text):
    wordDict = {}
    words = text.split()
    for word in words:
        if len(word) in wordDict:
            wordDict[len(word)] += 1
        else:
            wordDict[len(word)] = 1
    
    return wordDict
text = "it is what it is is is"
print(lengthFrequency(text))




'''Problem 3. write a fucntion lengthFreq2() that takes 1 parameter:
1. text, a string containing words and white spaces.
The function returns a dictionary of key:value pairs, where the key is
the length of a word and
the value is list of all words in that length.
For example:
if text = "it is what it is is is" the function returns
{2:['it','is','it','is','is','is'], 4:['what']'''



'''Problem 4. modify problem 3 to have a distinct list of words in a particular length...
For example:
if text = "it is what it is is is" the function returns
[2:['it','is'], 4:['what']'''



