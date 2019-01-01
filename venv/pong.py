import turtle
import random
import winsound

window = turtle.Screen()
window.title("Pong by @Harry")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
if random.random() < 0.5:
    ball.dx = 0.15
else:
    ball.dx = -0.15

if random.random() < 0.5:
    ball.dy = 0.15
else:
    ball.dy = -0.15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Function
def paddleAUp():
    y = paddleA.ycor()
    if (y <= 300):
        y += 20
    paddleA.sety(y)


def paddleADown():
    y = paddleA.ycor()
    if (y >= -300):
        y -= 20
    paddleA.sety(y)


def paddleBUp():
    y = paddleB.ycor()
    if (y <= 300):
        y += 20
    paddleB.sety(y)


def paddleBDown():
    y = paddleB.ycor()
    if (y >= -300):
        y -= 20
    paddleB.sety(y)


# Keyboard Binding
window.listen()
window.onkey(paddleAUp, "w")
window.onkey(paddleADown, "s")
window.onkey(paddleBUp, "Up")
window.onkey(paddleBDown, "Down")

# Main Game Loop
while True:
    window.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border Checking
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >= 390:
        ball.goto(0,0)
        if random.random() < 0.5:
            ball.dx *= -1
    if ball.xcor() <= -390:
        ball.goto(0,0)
        if random.random() < 0.5:
            ball.dx *= -1
    #Paddle and Ball Collision
    if ball.xcor() >= 340 and ball.xcor() <= 350 and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
        ball.setx(340)
        scoreB += 1
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() <= -340 and ball.xcor() <= 350 and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
        ball.setx(-340)
        scoreA += 1
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))