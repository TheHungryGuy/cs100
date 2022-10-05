#Exercise 2

scoresList = []
numOfScores =  int(input('How many Scores?'))
bonusList = []

for num in range(numOfScores):
    scoresList.append(int(input('Enter Score: ')))


for list in scoresList:
    bonusList.append(list+5)
print("Original List: " + str(scoresList))
print("Bonus List: " + str(bonusList))


