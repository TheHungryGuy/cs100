'''
Antonio Arce
CS100 Section 031
HW 03, September 27,2022
'''

#1.	Write code that uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon, each with side length 100.



import turtle
paper = turtle.Screen()
pen = turtle.Turtle()

pen.up()
pen.goto(-200,0)
pen.down()
#draw triangle
for tri in range(3):
    pen.left(120)
    pen.forward(100)

#draw square
pen.up()
pen.forward(20)
pen.down()
for sqr in range(4):
    pen.forward(100)
    pen.left(90)
    
#draw pentagon
pen.up()
pen.forward(140)
pen.down()

for penta in range(5):
    pen.forward(100)
    pen.left(72)


paper.delay()
pen.reset()

#2.	Write code that uses turtle graphics to draw four concentric circles of radius 50, 100, 150 and 200.
paper = turtle.Screen()
pen.up()
for cir in range(4):
    radius=50*(cir+1) #CALCULATE RAD
    pen.right(90) #face down
    pen.forward(radius) #move size of the rad
    pen.right(270) #face back to start
    pen.down()
    pen.circle(radius)
    pen.up()
    pen.home() #back to center
    

paper.exitonclick()
#3.	Write code that uses the Python math module to compute and print out the values of
import math
    #a.	100!
print("The factorial of 100! is " + str(math.factorial(100)))
    #b.	the log (base 2) of 1,000,000
print("The log (base 2) of 1,000,000 is " + str(math.log2(1000000)))
    #c.	the greatest common divisor of 63 and 49
print("The greatest common divisor of 63 and 49 is " + str(math.gcd(63,49)))
