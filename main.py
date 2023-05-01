import turtle
import random
import time

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")
turtle_instance.penup()
turtle_instance.hideturtle()
turtle_instance.shape("turtle")
turtle_instance.shapesize(2)

hidden_turtle = turtle.Turtle()
hidden_turtle.hideturtle()
hidden_turtle.penup()
hidden_turtle.setposition(0, 300)

hidden_turtle2 = turtle.Turtle()
hidden_turtle2.hideturtle()
hidden_turtle2.penup()
hidden_turtle2.setposition(0, 350)
hidden_turtle2.color("blue")

clicks = 0
t = 20

hidden_turtle2.write(arg=f'score:{clicks}', move=False, align='center', font=("arial", 20, "normal"))
def clicking(x, y)  :
    global clicks
    hidden_turtle2.clear()
    clicks = clicks + 1
    hidden_turtle2.write(arg=f'score:{clicks}', move=False, align='center', font=("arial", 20, "normal"))

turtle_instance.onclick(clicking)

while t > 0:
    turtle_instance.hideturtle()
    hidden_turtle.write(arg=f"time:{int(t)}", move=False, align='center', font=("arial", 30, "normal"))
    turtle_instance.setposition(random.randint(-299, 299), random.randint(-299, 299))
    turtle_instance.showturtle()
    time.sleep(0.6)
    t -= 0.6
    hidden_turtle.clear()

turtle_instance.hideturtle()
turtle_instance.setposition(random.randint(-299, 299), random.randint(-299, 299))

hidden_turtle.write(arg="Game Over !!", move=False, align='center', font=("arial", 30, "normal"))

turtle.mainloop()
