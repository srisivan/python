

# Program to draw a STAR


import turtle


star = turtle.Turtle()

star.pencolor("red")


for i in range(70):
	star.forward(90)
	star.right(160)

turtle.done()