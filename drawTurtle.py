import turtle

def draw_square(square):
    
    for i in range(1,5):
        square.forward(100)
        square.right(90)

    


def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    square=turtle.Turtle()
    square.color("yellow")
    square.shape("turtle")
    square.speed(2)
    for i in range(0,36):
        draw_square(square)
        square.right(10)
    window.exitonclick()


draw_art()