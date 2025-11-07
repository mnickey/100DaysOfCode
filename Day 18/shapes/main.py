import turtle
import random

# Set the TURTLE mode to colormode allowing for RGB information to be used
turtle.colormode(255)  # This allows you to use RGB values from 0 to 255

# Create the turtle class called timmy
timmy = turtle.Turtle()

# Set the attributes for timmy
timmy.shape("turtle")
timmy.color("green")
timmy.pensize(5) # Set the width of the pen to see the lines easier
timmy.speed(0) # Set the speed of the turtle (0 is the fastest speed)

# set variables for shape drawing and random walk
move_forward = 10

# Set variables for random_walk only
direction = [0, 90, 180, 270]
drawing_count = 0
max_drawing_size = 500

# Set variables for shape drawing only
full_angle = 360
current_sides = 3 # set the minimum sides
total_sides = 10 # set the maximum (inclusive) sides

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Spirograph Drawing
def draw_spirograph(gap_size):
    for _ in range(360 // gap_size):
        timmy.speed(0)
        timmy.pensize(1)
        timmy.pencolor(get_random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)

draw_spirograph(5)

# Random Walk Drawing
drawing = True # Used for the while loop to see if the drawing should continue

while drawing:
    timmy.pencolor(get_random_color())
    timmy.setheading(random.choice(direction))
    timmy.forward(move_forward)
    drawing_count += 1
    if drawing_count > max_drawing_size:
        drawing = False

# SHAPE DRAWING
drawing = True # Used for the while loop to see if the drawing should continue

while drawing:
    # print(current_sides) # Debug used to assure that sides are incrementing up to total_sides
    timmy.pencolor(get_random_color()) # Set the pen color randomly
    for _ in range(current_sides):
        # timmy.pencolor(get_random_color()) # inside the loop makes each side a different color
        timmy.forward(move_forward)
        timmy.right(full_angle / current_sides)
    current_sides += 1
    if current_sides > total_sides:
        drawing = False

screen = turtle.Screen()
screen.exitonclick()
