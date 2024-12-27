from turtle import Turtle
Alignment = "center"
Font = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 255)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=Alignment, font=Font)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=Alignment, font=Font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
