import turtle



def drawPentagon(pen,sideLen): 
    pen.down()
    for i in range(5):
        pen.forward(sideLen)
        pen.right(360/5)

paper = turtle.Screen()
myPen = turtle.Turtle()
drawPentagon(myPen,100)
paper.exitonclick()
