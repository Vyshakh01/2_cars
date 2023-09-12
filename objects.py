from turtle import Turtle
import random
positions=[(-300,280),(-100,280),(100,280),(300,280)]
#shapes=["square","circle"]
class Objects():
    def __init__(self):
        super().__init__()
        self.objects_list=[]
        self.create_object()
        self.speed=0.03


    def create_object(self):
        if random.randint(1,14)==1:
            obj=Turtle()
            obj.penup()
            if random.randint(1,3)==1:
                shape="circle"
            else:
                shape="square"

            obj.shape(shape)
            obj.goto(random.choice(positions))
            obj.setheading(270)
            if obj.shape()=="square":
                obj.color("blue")
            elif obj.shape()=="circle":
                obj.color("red")
            self.objects_list.append(obj)
    def move(self):
        for obj in self.objects_list:
            obj.forward(10)





