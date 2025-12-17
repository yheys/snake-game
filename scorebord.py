from turtle import Turtle

class Score_bord(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}",move=False,align="center",font=("Courier",20,"normal"))
        self.hideturtle()

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}", move=False, align="center", font=("Arial", 20, "normal"))

    def end(self):
        self.goto(0,0)
        self.write(f"Game Over!", move=False, align="center", font=("Arial", 20, "normal"))

