
from turtle import Screen
import time
from food import Food

from snake import Snake

from scoreboard import Scoreboard



#set up screen
screen = Screen()
screen.setup(width= 600,height=600)
screen.bgcolor('black')
screen.title('snake game')


#setup screen animation : 
screen.tracer(n=0)
#the animation on the screen is turned off , 
# behind the scene all the code is run but the result isnt shown yet until

#the method update is called ==> to avoid the delay in updating animation
#create a snake body




snake= Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key='Up',fun= snake.up )
screen.onkey(key='Down',fun= snake.down )

screen.onkey(key='Left',fun= snake.left )

screen.onkey(key='Right',fun= snake.right )






game_is_on = True

while game_is_on:

    snake.move()
    screen.update()
    time.sleep(0.1)

    #detect collision with food

    if snake.head.distance(food) <15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    #detect colision with wall
    if snake.head.xcor()>280 or  snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on= False
        scoreboard.game_over()

    #detect colision with tail

    for seg in snake.segments[1:]:
        
        if snake.head.distance(seg) <10:
            game_is_on =False
            scoreboard.game_over()
        















screen.exitonclick()