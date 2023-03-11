from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

continue_pong = True


def end_pong():
    global continue_pong
    continue_pong = False


screen.update()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(end_pong, "Escape")

game_speed = 40

while continue_pong:
    screen.update()
    ball.move()

    # detect collision with top/bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    right_condition = ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_dir > 0
    left_condition = ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_dir < 0
    if right_condition or left_condition :
        ball.bounce_x()
        game_speed *= 1.3

    # detect collision with right wall
    if ball.xcor() > 380:
        ball.bounce_x()
        ball.home()
        scoreboard.l_score += 1
        game_speed = 30

    # detect collision with left wall
    if ball.xcor() < -380:
        ball.bounce_x()
        ball.home()
        scoreboard.r_score += 1
        game_speed = 30

    scoreboard.display_score()

    time.sleep(1 / game_speed)


screen.exitonclick()