import turtle
turtle.colormode(255)


class Border(turtle.Turtle):

    def __init__(self, s_width, s_height):
        super().__init__()

        self.screen_half_width = s_width / 2
        self.screen_half_height = s_height / 2
        self.hideturtle()
        self.speed(10)
        self.color((90, 45, 67), "red")
        self.pensize(2)
        self.penup()
        self.border_half_height = (self.screen_half_height - 50)
        self.border_half_width = (self.screen_half_width - 50)
        self.goto(x=-self.border_half_width, y=-self.border_half_height)
        self.pendown()

        # make rectangle
        self.forward(2*self.border_half_width)
        self.left(90)
        self.forward(2*self.border_half_height)
        self.left(90)
        self.forward(2*self.border_half_width)
        self.left(90)
        self.forward(2 * self.border_half_height)

