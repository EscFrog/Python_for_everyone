import turtle as t
import random

# set enemy
enemyt = t.Turtle()
enemyt.shape("turtle")
enemyt.color("red")
enemyt.speed(0)
enemyt.up()
enemyt.goto(0, 200)

# set food
food = t.Turtle()
food.shape("circle")
food.color("green")
food.speed(0)
food.up()
food.goto(0, -200)

# define moving function
def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)
    ang = enemyt.towards(t.pos())
    enemyt.setheading(ang)
    enemyt.forward(9)
    if t.distance(food) < 12:
        star_x = random.randint(-230,230)
        star_y = random.randint(-230,230)
        food.goto(star_x, star_y)
    if t.distance(enemyt) >= 12:
        t.ontimer(play, 100)

t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()

play()

t.mainloop()