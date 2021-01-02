import turtle
import time
from paddle import Paddle
from border import Border
from ball import Ball
from score import Score
from level import Level
from pygame import mixer

mixer.init()
mixer.music.load("sounds/background-music-energy.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

turtle.colormode(255)

# screen setup
screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('grey')
screen.title("Pong Game")

# Border setup
border = Border(s_width=SCREEN_WIDTH, s_height=SCREEN_HEIGHT)

# paddle setup
paddle = Paddle(border_half_height=border.border_half_height, border_half_width=border.border_half_width)
paddle.goto((-1) * (SCREEN_WIDTH / 2 - 60), 0)

# ball setup
ball = Ball(border_half_height=border.border_half_height, border_half_width=border.border_half_width)

# score setup
score = Score(s_width=SCREEN_WIDTH, s_height=SCREEN_HEIGHT)

# level setup
level = Level(s_width=SCREEN_WIDTH, s_height=SCREEN_HEIGHT)

screen.update()

# paddle movement handle
screen.listen()
screen.onkeypress(key="Up", fun=paddle.move_up)
screen.onkeypress(key="Down", fun=paddle.move_down)

# play game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.001)
    ball.move()
    if ball.xcor() > paddle.xcor() + 20:
        pass

    # collision with paddle
    elif ball.xcor() >= paddle.xcor() + 19 and abs(paddle.ycor() - ball.ycor()) <= 60:
        ball.bounce(max_xcor=paddle.xcor() + 19, max_ycor=ball.max_ycor)
        score.update(1, screen=screen)
        paddle_contact_sound = mixer.Sound("sounds/paddle-contact-with-ball.mp3")
        paddle_contact_sound.play()
        if score.score % 3 == 0:
            level.increase_level()
            ball.increase_speed()

    # ball touched to the left side border
    else:
        game_is_on = False
        ball.stop(screen=screen)
        game_over_sound = mixer.Sound("sounds/game-over.mp3")
        game_over_sound.play()
        ball.goto(0, 0)
        score.update(0, screen=screen)
        screen.update()
        mixer.music.pause()

screen.exitonclick()
