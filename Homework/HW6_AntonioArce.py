'''
Antonio Arce
CS100 Section 031
HW 06 October 18,2022
'''
#1 -a

#function that checks last letter in a list and sees if they are in the given letters
#then returns a list
def hasFinalLetter(strList,letters):
    finalList = []
    for lastChar in strList:
        if lastChar[-1:] in letters:
            finalList.append(lastChar)
    return finalList
#b
#test cases
words1= ["orange","monkey", "EAGLE"]
words2= ["apple", "GRAPES"] 
words3= ["ahhhhhh","apple"]
vowels = "aeiouAEIOU"
vowelsLow = "aeiou"
vowelsUp = "AEIOU"

print(hasFinalLetter(words1,vowels))
print(hasFinalLetter(words2,vowelsLow))
print(hasFinalLetter(words3,vowelsUp))

#2 -a
#function isDivisible should create and return a list of all the ints in the range from 1 to maxInt (not 
#including maxInt) that are divisible of both ints in twoInts.

def isDivisible(maxInt,twoInts):
    divisble = [];
    for num in range(1,maxInt):
        if num%twoInts[0]==0 and num%twoInts[1]==0:
            divisble.append(num);
    return divisble;

#b
#test cases

maxA=45
maxB=20
maxC=5
twoA = (3,5)
twoB = (2,5)
twoC = (1,7)

print(isDivisible(maxA,twoA))
print(isDivisible(maxB,twoB))
print(isDivisible(maxC,twoC))