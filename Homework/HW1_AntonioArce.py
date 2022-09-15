'''
Antonio Arce
CS100 Section 031
HW 01, September 13,2022
'''
#Exercise 5b
from tkinter import N


students=30
days=31
hours=24

#Exercise 5c
speed=5.4
chapter=10.1
version=9.23

#Exercise 5d
fName="Jeff"
lName="Bezos"
company="Amazon"

#Exercise 1.1
#1
'''
It throws an error
'''
#2
'''
It throws an error for unterminated string
'''
#3
'''
Python treats the number as a positive 2 and prints it out correctly. 
When doing 2++2 it prints out the result of 4 correctly.
'''

#print(2++2)
#Exercise 1.2
#1
seconds= 42*60+42
print(seconds) #2562 seconds

#2
km=1.61
miles = 10/km
print(miles) #6.21miles =10km

#3
paceInSecs = (miles/seconds) 
print(paceInSecs) #0.0024mile/sec
mins = 42+42/60
print (mins)

speedPerMins = miles/mins
print (speedPerMins) #0.145 miles/min

hour= mins/60
print (hour) #.71 hours

mph= miles/hour
print(mph)
#8.7mph


#Exercise 2.1
#1
'''
A syntax error would occur for 42=y
X would equal 1 and y would equal 1
The semi colon still works.
the period cause a syntax error.
It looks for an xy variable which is not defined. 

'''


#Exercise 2.2
#1
import math
radius = 5.0
print((4 * math.pi * (radius ** 3))/3)
#2
books = 0.6 * 24.95
price = books * 60 + (3 * 59*.75)
print(price)

#3
def toSeconds(time):
    minutes,seconds = time.split(":")
    return (int(minutes)*60) + int(seconds)

def timeToSecs(time):
    hours,minutes = time.split(":")
    return (int(hours)*60*60)+ (int(minutes)*60)
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

startTime = timeToSecs("6:52")
secondsTraveled = ( (toSeconds("8:15")* 1 ) + (toSeconds("7:12") *3 ) + (toSeconds("8:15") * 1 ) )

endTime = startTime+secondsTraveled
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%d:%02d:%02d" % (hour, minutes, seconds)

print(convert(endTime))   

