import turtle

def drawSquare(someTurtle):
    for x in range(0,4):
        someTurtle.forward(100)
        someTurtle.right(90)


def drawArt():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()

    for i in range(1,36):
        drawSquare(brad)
        brad.right(10)

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    window.exitonclick()



drawArt()
