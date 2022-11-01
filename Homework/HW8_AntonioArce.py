'''
Antonio Arce
CS100 Section 031
HW 08 November 01,2022
'''

'''
Problem 1
This problem provides practice using a while True loop.
Write a function named twoWords that gets and returns two words from a user. The first word is of a 
specified length, and the second word begins with a specified letter.

The function twoWords takes two parameters:
1. an integer, length, that is the length of the first word and
2. a character, firstLetter, that is the first letter of the second word. The second word may begin with 
either an upper or lower case instance of firstLetter.

The function twoWords should return the two words in a list. Use a while True loop and a break statement 
in the implementation of twoWords.

The following is an example of the execution of twoWords:

print(twoWords(4, 'B'))
Enter a 4-letter word please: two
Enter a 4-letter word please: one
Enter a 4-letter word please: four
Enter a word beginning with B please: apple
Enter a word beginning with B please: pear
Enter a word beginning with B please: banana
['four', 'banana']
'''

def twoWords(length,firstLetter):
    twoList = []
    while True:
        word = input("Enter a {}-letter word:".format(length))     
        if len(word) == length:
            twoList.append(word)
            break;
    while True:
        word = input("Enter a word Begining with {}:".format(firstLetter))
        if word[0].lower() == firstLetter.lower():
            twoList.append(word)
            break;
    return twoList    
print(twoWords(3, 'A'))