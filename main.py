import colorgram as colorgram
import turtle as turtle_module
import random

# Spirograph
# tim = t.Turtle()
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     col = (r, g, b)
#     return col
#
#
# tim.pensize(3)
# tim.speed("fastest")
# directions = [0, 90, 180, 270]
# screen = t.Screen()
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(150)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)
# screen.exitonclick()

# Hirst painting
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
number_of_dots = 100

def get_colors():
    colors = colorgram.extract('image.jpg', 30)
    rgb_colors = []

    for n in colors:
        r = n.rgb.r
        g = n.rgb.g
        b = n.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    rgb_colors.pop(0)
    return rgb_colors
rgb_colors = get_colors()


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dot_count %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()