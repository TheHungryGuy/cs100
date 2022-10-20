#Emrehan Seferoglu
#Antonio Arce
def vowelWords(text):
    words=text.split()
    vowels="aeiouAEIOU"
    count = 0
    for first in words:
        if first[0] in vowels:
            count+=1
    return count

phrase = "Hi everyone It is what it is python is fun"

print(vowelWords(phrase))