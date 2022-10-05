'''
Antonio Arce
CS100 Section 031
HW 04, September 27,2022
'''

""" 
1. Write Python code that does the following:
a. Assigns the values 3, 4 and 5 to the variables a, b and c, respectively.
b. Write an if statement that prints “OK” if a is less than b
c. Write an if statement that prints “OK” if c is less than b
d. Write an if statement that prints “OK” if the sum of a and b is equal to c
e. Write an if statement that prints “OK” if the sum of a squared and b squared equals c squared.

2. Repeat the previous problem with the additional requirement that “NOT OK” is printed if the 
condition is false.
"""
a=3;
b=4;
c=5;

#b
if(a<b):
    print("OK")
else:
    print("NOT OK")

#c
if(c<b):
    print("OK")
else:
    print("NOT OK")

#d
if((a+b)==c):
    print("OK")
else:
    print("NOT OK")

#e
if((a^2+b^2)==c^2):
    print("OK")
else:
    print("NOT OK")

""" 
3. Write a program that asks the user for a color, a line width, a line length and a shape. Assume that 
the user will specify a shape that is either a line, a triangle, or a square. Use turtle graphics to draw 
the shape that the user requests of the size, color, line width and line length that the user requests. 
For example, if these are the user choices for color, width, line length and shape, the blue triangle 
below would be correct graphical output
 what color? blue
what line width? 25
what line length? 100
line, triangle or square? triangle 
"""
color = input("What Color? ")
lnWidth = int(input("What line width? "))
lnLength = int(input ("What line length?"))
shape = input("Line, Triangle, or Square?")
shape = shape.lower()
#python switch statment for shape
match shape:
    case "line":
        import turtle
        paper = turtle.Screen()
        pen = turtle.Turtle()
        pen.color(color)
        pen.width(lnWidth)
        pen.forward(lnLength)
    case "triangle":
        import turtle
        paper = turtle.Screen()
        pen = turtle.Turtle()
        pen.color(color)
        pen.width(lnWidth)
        for i in range(3):
            pen.forward(lnLength)
            pen.right(120)

    case "square":
        import turtle
        paper = turtle.Screen()
        pen = turtle.Turtle()
        pen.color(color)
        pen.width(lnWidth)
        for i in range(4):
            pen.forward(lnLength)
            pen.right(90)
paper.exitonclick()
