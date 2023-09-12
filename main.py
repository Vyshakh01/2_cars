import turtle
from drawer import Drawer
from car import Car
import time
from objects import Objects
from scoreboard import Scoreboard
screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("2 WAYS")
screen.tracer(0)
drawer=Drawer()
objects=Objects()
scoreboard=Scoreboard()
r_car=Car("yellow",(100,-250))
l_car=Car("green",(-100,-250))
screen.listen()
screen.onkey(fun=r_car.move_right,key="Right")
screen.onkey(fun=r_car.move_left,key="Left")
screen.onkey(fun=l_car.move_right,key="d")
screen.onkey(fun=l_car.move_left,key="a")
is_game_on=True
while is_game_on:

    objects.create_object()
    screen.update()
    time.sleep(objects.speed)
    objects.move()
    for obj in objects.objects_list:
        if l_car.distance(obj)<5 and obj.shape()=="square":
            obj.goto(1200,1200)
            scoreboard.point()
        if r_car.distance(obj)<5 and obj.shape()=="square":
            obj.goto(1200,1200)
            scoreboard.point()
        if r_car.distance(obj) < 5 and obj.shape() == "circle":
            scoreboard.game_over()
            scoreboard.update_high()
            is_game_on=False
        if l_car.distance(obj) < 5 and obj.shape() == "circle":
            scoreboard.game_over()
            scoreboard.update_high()
            is_game_on=False
        if r_car.xcor()>300 or r_car.xcor()<0:
            scoreboard.game_over()
            scoreboard.update_high()
            is_game_on=False
        if l_car.xcor()>0 or l_car.xcor()<-300:
            scoreboard.game_over()
            scoreboard.update_high()
            is_game_on=False
        # if scoreboard.score>5:
        #     objects.increase_speed(1)






    
screen.exitonclick()
