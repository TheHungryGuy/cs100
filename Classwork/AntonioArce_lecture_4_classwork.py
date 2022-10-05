'''
Create two empty list: even_nums_list and odd_nums_list
add the even numbers to even list from (1-100) and odd
then print both list
'''
#2
even_nums_list=[]
odd_nums_list=[]

for i in range(1,101):
    if(i%2 == 0):
        even_nums_list.append(i)
    else:
        odd_nums_list.append(i)

print(even_nums_list)
print()
print(odd_nums_list)


#3
myName="Antonio"
userName= input('What is your name?')

if(myName[0]== userName[0].upper()):
    import turtle
    paper = turtle.Screen()
    pen = turtle.Turtle()

    pen.right(-120)
    pen.forward(60)
    pen.right(-120)
    pen.forward(60)
    pen.backward(30)
    pen.left(120)
    pen.forward(30)
    paper.exitonclick()

else:
    print("Hello {}!".format(userName))


