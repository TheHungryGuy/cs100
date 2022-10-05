#exercise 1
fruitList = ['apple','kiwi',"orange", "banana"]
vowels = 'aeiou'
count = 0

for fruit in fruitList:
    if fruit[0::-1] in vowels:
        count +=1

print('count of words start with a vowel',count)

#exercise 2

gradeList = [87,65,87,98,87,56]
aScore = 82
count = 0

for grades in gradeList:
    if grades >= aScore:
        count +=1

print('A grades: ',count)

#exercise 3
lst = [87,65,87,98,87,56]

countodd = 0

counteven = 0

for number in lst:
    if number %2 == 0:
        counteven = counteven + 1
    else:
        countodd = countodd + 1

oddlist = [countodd, counteven]


print(oddlist)

#exercise 4
emptylst = []

for score in lst:
    if score not in emptylst:
        emptylst.append(score)

print(emptylst)