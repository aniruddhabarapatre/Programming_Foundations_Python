import turtle

def draw_name(name_turtle):
    # Alphabet A
    name_turtle.pu()
    name_turtle.setx(-200)
    name_turtle.pd()
    name_turtle.left(60)
    name_turtle.forward(200)
    name_turtle.right(120)
    name_turtle.forward(200)
    name_turtle.backward(100)
    name_turtle.left(240)
    name_turtle.forward(100)

    # Alphabet B
    name_turtle.pu()
    name_turtle.setpos(10,180)
    name_turtle.pd()
    name_turtle.left(90)
    name_turtle.forward(180)
    name_turtle.left(90)
    name_turtle.forward(30)
    name_turtle.circle(45,180)
    name_turtle.forward(30)
    name_turtle.backward(30)
    name_turtle.left(180)
    name_turtle.circle(45,180)
    name_turtle.forward(30)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    name = turtle.Turtle()
    name.shape("turtle")
    name.color("Yellow")
    draw_name(name)

    window.exitonclick()

draw_art()
