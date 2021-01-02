import turtle

turtle.colormode(255)


class Level(turtle.Turtle):
    def __init__(self, s_width, s_height):
        super(Level, self).__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 0
        self.goto(-s_width / 2 + 140, s_height / 2 - 40)
        self.pencolor((1, 253, 197))
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.current_level += 1
        self.write(arg=f"Level : {self.current_level}", align="center", font=("courier", 20, "bold"))

