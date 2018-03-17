#changing colours
import turtle

painter = turtle.Turtle()

painter.speed(100)

painter.pencolor("blue")

for i in range(100):
    painter.forward(50)
    painter.left(123) #counter clockwise

painter.pencolor("red")

for i in range(100):
    painter.forward(100)
    painter.left(123)

painter.pencolor("green")

for i in range(100):
    painter.forward(150)
    painter.left(123)

turtle.done()
