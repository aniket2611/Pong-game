import turtle

turtle.colormode(255)


class Score(turtle.Turtle):
    def __init__(self, s_width, s_height):
        super(Score, self).__init__()
        self.penup()
        self.pencolor((1, 253, 197))
        self.hideturtle()
        self.goto(s_width/2 - 170, s_height / 2 - 40)
        self.score = -1
        self.update(1, False)

    def update(self, game_is_on, screen):
        self.clear()
        if game_is_on:
            self.score += 1
            self.write(arg=f"Your score : {self.score}", align="center", font=("courier", 20, "bold"))
        else:
            screen.clear()
            screen.bgcolor('grey')
            screen.title("Pong Game")
            self.goto(0, 40)
            self.write(arg=f"Game Over", align="center", font=("courier", 40, "bold"))
            self.goto(0, -40)
            self.write(arg=f"Your final score is {self.score}", align="center", font=("courier", 40, "bold"))


