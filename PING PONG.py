from turtle import Turtle, Screen
from paddle import Paddple
from ball import Ball
from scoreboard import Scoreboard
import time

# STEP ONE CREATE THE SCREEN
my_screen = Screen()
my_screen.bgcolor('Black')
my_screen.setup(width=800, height=600)
my_screen.title('PING PONG')
my_screen.tracer(0)

# STEP TWO CREATE A MOVE PADDLE
right_paddle = Paddple(350, 0)
left_paddle = Paddple(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(right_paddle.up, 'w')
my_screen.onkey(right_paddle.down, 's')

my_screen.onkey(left_paddle.up, 'Up')
my_screen.onkey(left_paddle.down, 'Down')

game_is_on = True

while game_is_on:
    my_screen.update()
    ball.move()

    # DETECT COLLISION WITH WALL
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # DETECT COLLISION WITH PADDLES
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() > -320):
        ball.bounce_x()


    # DETECT R PUDDLE MISSED
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_score_plusone()

    # DETECT L PUDDLE MISSED
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_score_plusone()


my_screen.exitonclick()
