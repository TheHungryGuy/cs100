'''
Antonio Arce
CS100 Section 031
HW 05 October 04,2022
'''

#1
months =  ['January','February','March','April','May','June','July','August','September','October','November','December']
#print out each month that begins with letter j
for j in months:
    if j[0] == 'J':
        print (j)

#2 for loop between 0-99 

for i in range(100):
    if i%2 == 0 and i%5 == 0:
        print (i)


#3  Write a for loop that prints out all the vowels in horton in the order they appear in horton.
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letters in horton:
    if letters in vowels:
        print (letters)
