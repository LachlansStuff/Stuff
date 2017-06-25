#IMPORTING
import turtle

#INITIALISING THE TURTLE
my_turtle = turtle.Turtle()
my_turtle.speed(0.5)

#FUNCTION TO MAKE SQUARE
def square():
    for i in range (4):
        my_turtle.forward(100)
        my_turtle.right(90)

#FUNCTION TURN A BIT AFTER DRAWING A SQUARE
def turn(angle):
    my_turtle.right(angle)

#CALLING AND LOOPING THE FUNCTIONS
for i in range(1000):
    square()
    turn(11)

#FINISHED!
turtle.done
