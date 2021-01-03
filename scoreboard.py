from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.level = 1
        self.update_board()

    def update_board(self):
        self.write(f'Level:{self.level}', align='left', font=FONT)

    def add_score(self):
        self.clear()
        self.level += 1
        self.update_board()

    def game_over(self):
        self.write('Game Over')


