import turtle

DISTANCE_TO_MOVE = 10
screen = turtle.Screen()


class Paddle(turtle.Turtle):
    def __init__(self, border_half_height, border_half_width):
        super().__init__()
        self.penup()
        self.max_y_cor = border_half_height
        self.shape("square")
        self.color("black", "blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.speed(10)

    def move_up(self):
        for i in range(2):
            if self.max_y_cor - (self.ycor() + 50) >= DISTANCE_TO_MOVE:
                self.forward(DISTANCE_TO_MOVE)

    def move_down(self):
        for i in range(2):
            if (self.ycor() - 50) + self.max_y_cor >= DISTANCE_TO_MOVE:
                self.backward(DISTANCE_TO_MOVE)
