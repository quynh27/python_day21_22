
from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self) :
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  #10x10 pixels size
        self.color('DeepPink')
        self.speed('fastest')
        
        self.refresh()
    

    def refresh(self):  # food go to a new random location every time the refresh method is called
        self.goto(random.randint(-280,280),random.randint(-280,280))



