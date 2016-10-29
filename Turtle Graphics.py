#Homework 2
#3. Turtle Graphics
#Neil Opena 110878452
from turtle import *
bob = Turtle()

screen = bob.getscreen()
bob.speed(0)
rows = int(screen.numinput("How many rows?","How many rows?",5,1,10))
columns = int(screen.numinput("How many columns?","How many columns?",5,1,10))
length = int(screen.numinput("How long is the side of the square?","How long is the side of the square?",25,10,50))

color_1 = screen.textinput("What is the first color?","What is the first color?")
color_2 = screen.textinput("What is the second color?","What is the second color?")
color_3 = screen.textinput("What is the third color?","What is the third color?")


loc_y = 0 - length
fill = ''

#Works for columns: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
value = 1
4
def draw_square():
    global bob
    bob.color("black",fill)
    bob.begin_fill()
    for i in range(2):
        bob.pendown()
        bob.forward(length)
        bob.left(90)
        bob.forward(length)
        bob.left(90)
    bob.end_fill()
    bob.forward(length)
    bob.penup()


if columns == 4 or columns == 7 or columns == 10:
    for x in range(rows):
        for i in range(columns):
            bob.setheading(0)
            if value == 1:
                fill = color_1
            elif value == 2:
                fill = color_2
            elif value == 3:
                fill = color_3
            elif value == 0:
                value = 0
                fill = color_3   
            else:
                value = 1
                fill = color_1
            value = value + 1
            draw_square()
        bob.goto(0,loc_y)
        value = value - 2  
        loc_y = loc_y - length
     
elif columns % 3 == 0:
    for x in range(rows):
        for i in range(columns):
            bob.setheading(0)
            if value == 1:
                fill = color_1
            elif value == 2:
                fill = color_2
            elif value == 3:
                fill = color_3
            else:
                value = 1
                fill = color_1
            value = value + 1
            draw_square()
        bob.goto(0,loc_y)
        value = value - 1
        loc_y = loc_y - length

else:
    for x in range(rows):
        for i in range(columns):
            bob.setheading(0)
            if value == 1:
                fill = color_1
            elif value == 2:
                fill = color_2
            elif value == 3:
                fill = color_3
            else:
                value = 1
                fill = color_1
            value = value + 1
            bob.color("black",fill)
            draw_square()
        bob.goto(0,loc_y)
        loc_y = loc_y - length

