'''
Antonio Arce
CS100 Section 031
HW 02, September 20,2022
'''

'''
1.	This question practices the use of a list method. Assign to the variable grades a list of 10 letter grades from among 'A', 'B', 'C', 'D', and 'F'. For example:
 	grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
 	Write a Python expression that creates a list named frequency, in which the elements are the number of times each of the letters A, B, C, D and F appear in grades. For example, for the above value of grades, the following would be correct output:
 	frequency = [4, 2, 2, 0, 2]
 	Your expression must give the correct values for any list of grades, not just the one in your list. Hint: use the list method count.
'''
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']

frequency =[]
#for loop to count letters in list and append to frequency list
for characters in ['A','B','C','D','F']:
    charCount=grades.count(characters)
    frequency.append(charCount)

print(frequency)


'''    
2.	This question practices list membership, list indexes and list slices.
a.	Write a Python statement that creates a list named dog_breeds that contains the elements 'collie', 'sheepdog', 'Chow', and 'Chihuahua' in the order given.
b.	Write a Python statement that uses list slicing to create a list herding_dogs that is made up of the first two elements of dog_breeds.
c.	Write a Python statement that uses list indexing to create a list tiny_dogs that is made up of the last element of dog_breeds.
d.	Write a Python statement that tests whether 'Persian' is in the list dog_breeds and prints either True or False depending on the answer.
'''
#2a
dog_breeds =['collie', 'sheepdog', 'Chow','Chihuahua']
print(dog_breeds)
#2b
herding_dogs = dog_breeds[0:2]
print(herding_dogs)
#2c
tiny_dogs = dog_breeds[-1]
print(tiny_dogs)
#2d
if'Persian' in dog_breeds:
	print("Persian found")
else:
	print("Persian not found")