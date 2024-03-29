from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()

    def refresh(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1

    def reset_position(self):
        self.setpos(0,0)
        self.bounce_x()

    def speed_increase(self, speed):
        new_x = self.xcor() + self.x_move * speed
        new_y = self.ycor() + self.y_move * speed
        self.goto(new_x, new_y)

