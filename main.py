import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")
turtle_instance.penup()
turtle_instance.hideturtle()
turtle_instance.shape("turtle")
turtle_instance.shapesize(2)

time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.setposition(0, 300)

hidden_turtle2 = turtle.Turtle()
hidden_turtle2.hideturtle()
hidden_turtle2.penup()
hidden_turtle2.setposition(0, 350)
hidden_turtle2.color("blue")

clicks = 0
t = 20

hidden_turtle2.write(arg=f'score:{clicks}', move=False, align='center', font=("arial", 20, "normal"))


def clicking(x, y):
    global clicks
    hidden_turtle2.clear()
    clicks = clicks + 1
    hidden_turtle2.write(arg=f'score:{clicks}', move=False, align='center', font=("arial", 20, "normal"))


turtle_instance.onclick(clicking)


def turtle_instance_move():
    turtle_instance.hideturtle()
    turtle_instance.setposition(random.randint(-299, 299), random.randint(-299, 299))
    turtle_instance.showturtle()
    screen.update()
    if t > 0:
        screen.ontimer(turtle_instance_move, 600)
    else:
        turtle_instance.hideturtle()


def time_turtle_move():
    global t
    t -= 1
    time_turtle.clear()
    time_turtle.write(arg=f"time:{int(t)}", move=False, align='center', font=("arial", 30, "normal"))
    if t > 0:
        screen.ontimer(time_turtle_move, 1000)
    else:
        time_turtle.clear()
        time_turtle.write(arg="Game Over !!", move=False, align='center', font=("arial", 30, "normal"))


turtle_instance_move()
time_turtle_move()


turtle.mainloop()
