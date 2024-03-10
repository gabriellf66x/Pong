import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True

paddle = Paddle((380, 0))
ball = Ball()
npc_paddle = Paddle((-380, 0))
score_count = Scoreboard()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

screen.onkey(npc_paddle.up, "w")
screen.onkey(npc_paddle.down, "s")
speed = 0
while game_is_on:
    screen.update()
    if speed == 0:
        ball.refresh()
    else:
        ball.speed_increase(speed)
    time.sleep(0.04)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.xcor() > 330 or ball.distance(npc_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        speed += .2

    if ball.xcor() > 380:
        score_count.l_point()
        ball.reset_position()
        speed = 0

    if ball.xcor() < -380:
        score_count.r_point()
        ball.reset_position()
        speed = 0


screen.exitonclick()
