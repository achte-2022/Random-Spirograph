#Importing Libraries
import turtle
import random

#Constants
MAX_INTENSITY = 255
ANGLES = [0, 90, 180, 270]
SHAPE = 'classic'
SPEED = 'fastest'
LINE_WIDTH = 5
WALK_LENGTH = 20
NUM_WALKS = 500
SPIROGRAPH_RADIUS = 15
BG_COLOR = 'black'

#Color Setup
turtle.colormode(MAX_INTENSITY)

#Function to Generate Random Color
def random_color():
    red = random.randint(0, MAX_INTENSITY)
    green = random.randint(0, MAX_INTENSITY)
    blue = random.randint(0, MAX_INTENSITY)
    return (red, green, blue)


#Random Walk Algorithm
def random_walk(turtle_object, num_walks, walk_length, radius):

    for _ in range(num_walks):
        angle = random.choice(ANGLES)
        color = random_color()
        turtle_object.color(color)
        turtle_object.right(angle)
        turtle_object.penup()
        turtle_object.forward(walk_length)
        turtle_object.pendown()
        turtle_object.circle(radius)
    turtle_object.hideturtle()

#Object Setup
turtle_object = turtle.Turtle()
turtle_object.shape(SHAPE)
turtle_object.width(LINE_WIDTH)
turtle_object.speed(SPEED)
window = turtle.Screen()
window.bgcolor(BG_COLOR)

random_walk(turtle_object, NUM_WALKS, WALK_LENGTH, SPIROGRAPH_RADIUS)
print("Done.")
window.exitonclick()
