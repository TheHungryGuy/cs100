"""
Name: Antonio Arce
Class number: CS100-035
Assignment: Lecture2 Classwork 
"""

print("#Q1")
"""
Take the square of number 4 using the two methods we learned in class (hint: one of them you need to use the math module)
"""
import math 
print(4**2)
print(math.pow(4,2))

print()

print("#Q2")
"""
Take the square root of 4 using the two methods we learned in class (hint: one of them you need to use the math module)
"""
print(math.sqrt(4))
print(4**.5)

print()
print("#Q3")
"""
word = 'hello'
# Print out 'e' using indexing
"""
word = "hello"
print(word[1])

print()
print("#Q4")
"""
word ='hello'
# Reverse the above string using slicing
"""
revWord = word[len(word)-1::-1]
print(revWord)

print()
print("#Q5")
"""
Word= ‘hello’
Given the string hello above, give two methods of producing the letter 'o' using indexing.
"""
# Method 1:
print(word[4])
# Method 2:
print(word[-1])


print()
print("#Q6")
"""
Reassign 'hello' in the nested list below to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
"""
list3 = [1,2,[3,4,'hello']]
list3[-1][-1]='goodbye'
print(list3)



print()
print("#Q7")
"""
Sort the list below:
num_list = [5,3,4,6,1]
"""

num_list = [5,3,4,6,1]
print(sorted(num_list))

print()
print("#Q8")
"""
What is the main difference between lists and tuples? 
"""
print("The main difference is tuples cannot be changed and are immutable,\nwhile list are mutable and can be changed.")
print()
print("#Q9")
"""
Write a Boolean expression that shows whether a number is even (ex: check if 9 is even), then print it out. 
"""
print("Check if 9 is even\n")
number =9
even = bool(number%2==0)
print(even)
print()
print("#Q10")
"""
Sort the list below in descending order
Num_list = [78, 56,31,100,141,29]
"""
Num_list = [78, 56,31,100,141,29]
print(sorted(Num_list,reverse=True))


print()
print("#Q11")
"""
Create an empty list called ‘grades_list’, then add the following grades to it (one grade at a time): 99, 82, 56, 76, 81.
Then print the following: grades average, the minimum score, and the maximum score.
"""
grades_list=[]
grades_list.append(99)
grades_list.append(82)
grades_list.append(56)
grades_list.append(76)
grades_list.append(81)
print(grades_list)
avg = sum(grades_list)/len(grades_list)
min = min(grades_list)
max = max(grades_list)
print("Average: " +str(avg)+ " Min: " +str(min) + " Max: " +str(max) )


print()
print("#Q12")
"""
name = ‘Emily’
age = 21
print the following statement : ‘My name is Emily, and I’m 21 years old.’
Using the two methods we learned about. Note you should use the assigned variable (name and age) when writing the code. 
"""
name = 'Emily'
age = 21

print("My name is "+ name + ", and I\'m " + str(age) + " years old.")
print('My name is {}, and I\'m {} years old.'.format(name, age))