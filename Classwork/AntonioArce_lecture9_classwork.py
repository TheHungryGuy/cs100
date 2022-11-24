#Antonio Arce
#Emrehan Seferoglu

#EXERCISE 1

'''write a function getAverage() that takes one parameter:
1. filename, the name of a file containing students score information
(like those in scores.txt)
the function returns the average socre in the class (average score of all socres int eh file).
For example, if filename ='sccores.txt', the average is whatever average of
(95, 78, 92, 78, 80)
'''

def getAverage(filename):
    inFile = open(filename,'r')
    count = 0
    mean = 0
    for line in inFile:
        num = line.split()[-1]
        mean += int(num)
        count += 1
    return mean/count

print(getAverage("scores.txt"))   

#Exercise 2

'''write a function studetnsWithAs() that takes two parameters:
1. name1, the name of an input file containing students scores in this format:
studetnsName studetnScore
2.name2, the name of an output file to write to
The function writes to the output file the names of the studetns who got an A,
one name per line.For example, if name1 is "scores.txt" the output file should
contain
John
Jill
...
'''

def studentsWithAs(name1,name2):
    #open 1st file to read thru 
    aGradesList = []
    inputFile = open(name1,"r")
    #an A is >= to 90
    scores = inputFile.readlines()
    for line in scores:
        num = line.split()
        if int(num[-1]) >= 90:
            aGradesList.append(num[0])
    
    #open 2nd file to write to
    outputFile = open(name2,"w")
    for student in aGradesList:
        outputFile.write(student)
        outputFile.write("\n")
        
studentsWithAs("scores.txt","studentswithas.txt")