from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,240)
        self.score=0
        with open("highscore","r")as hs:
            self.highscore=int(hs.read())


        self.pencolor("white")
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"score:{self.score}\t best:{self.highscore}",font=("Courrier",40,"normal"),align="center")
    def point(self):
        self.score+=1
        self.update_score()
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAMEOVER", font=("Courrier", 40, "normal"), align="center")
    def update_high(self):
        self.goto(50,250)
        if self.score>self.highscore:
            self.highscore=self.score
            with open("highscore","w")as hs:
                hs.write(f"{self.highscore}")
            self.update_score()
