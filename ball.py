from turtle import Turtle
import time
from random import choice


class Ball(Turtle):
    def __init__(self, border_half_width, border_half_height):
        super(Ball, self).__init__()
        self.penup()
        self.color("orange", "red")
        self.shape("circle")
        self.border_half_width = border_half_width
        self.border_half_height = border_half_height
        self.max_xcor = border_half_width - 10
        self.max_ycor = border_half_height - 10
        direction = [-1, 1]
        self.x_move = 1 * choice(direction)
        self.y_move = 1 * choice(direction)

    def move(self):
        if self.max_xcor >= self.xcor() and self.max_ycor >= self.ycor() >= -self.max_ycor:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        else:
            self.bounce(self.max_xcor, self.max_ycor)

    def bounce(self, max_xcor, max_ycor):
        if self.ycor() > max_ycor or self.ycor() < -max_ycor:
            self.y_move *= (-1)
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        elif self.xcor() > max_xcor or self.xcor() < -max_xcor:
            self.x_move *= (-1)
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def stop(self, screen):
        while self.xcor() > -self.border_half_width + 9:
            screen.update()
            time.sleep(0.001)
            self.move()

    def increase_speed(self):
        increase_amount = 0.15
        if self.x_move < 0:
            self.x_move -= increase_amount
        else:
            self.x_move += increase_amount

        if self.y_move < 0:
            self.y_move -= increase_amount
        else:
            self.y_move += increase_amount
