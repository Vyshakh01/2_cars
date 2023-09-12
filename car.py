from turtle import Turtle
class Car(Turtle):
    def __init__(self,color,position):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=2)
        self.color(color)
        self.penup()
        self.goto(position)
    def move_left(self):
        new_x=self.xcor()-200
        self.goto(new_x,self.ycor())

    def move_right(self):
        new_x = self.xcor() + 200
        self.goto(new_x, self.ycor())