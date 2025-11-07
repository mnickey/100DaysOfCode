import random
import turtle
turtle.colormode(255)  # This allows you to use RGB values from 0 to 255

# colors = colorgram.extract("image.jpg", 30)
# print(colors[0].rgb[0])
# print(len(colors))
# my_colors = []
# for color in colors:
#     r = color.rgb[0]
#     b = color.rgb[1]
#     g = color.rgb[2]
#     color_tuple = (r, g, b)
#     my_colors.append(color_tuple)
#
# print(my_colors)
color_list = [(218, 103, 148), (35, 169, 102), (159, 87, 56), (143, 56, 81), (241, 97, 226),
              (114, 212, 173), (218, 156, 128), (166, 42, 23), (217, 101, 66), (224, 57, 82), (119, 137, 183),
              (78, 26, 37), (21, 201, 167), (159, 33, 151), (17, 140, 57), (42, 80, 125), (123, 28, 38),
              (49, 156, 186), (17, 87, 39), (133, 190, 234), (239, 154, 164), (233, 184, 164), (133, 233, 213),
              (101, 183, 103), (75, 48, 34), (161, 232, 177)]

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.speed(0)
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

timmy.hideturtle()
screen = turtle.Screen()
screen.exitonclick()
