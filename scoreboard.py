from turtle import Turtle
ALIGNMENT ='center'
FONT=('Courier',20,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x= 0,y=260)
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(arg=f'Score:{self.score}',align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score= self.score+1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER',align=ALIGNMENT,font=FONT)

        