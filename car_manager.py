from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.random_color = random.choice(COLORS)
        self.color(self.random_color)
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        self.random_number = random.randint(-250, 270)
        self.goto(300, self.random_number)
        self.move_forward()


    def move_forward(self):
        if self.xcor() > -280:
            new_speed = self.xcor() - STARTING_MOVE_DISTANCE
            self.goto(new_speed, self.ycor())
