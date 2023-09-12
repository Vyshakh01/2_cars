from turtle import Turtle
class Drawer(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(-200, -300)
        self.pendown()
        self.goto(-200, 300)
        self.penup()
        self.goto(0, -300)
        self.pendown()
        self.goto(0, 300)
        self.penup()
        self.goto(200, -300)
        self.pendown()
        self.goto(200, 300)