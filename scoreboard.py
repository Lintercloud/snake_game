from turtle import *

ALIGN = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self,):
       super().__init__()
       self.score = 0
       self.goto(0, 280)
       self.pencolor("white")
       self.hideturtle()
       self.up_data()

    def up_data(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGN)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT, align=ALIGN)

    def get_score(self):
        self.score += 1
        self.clear()
        self.up_data()