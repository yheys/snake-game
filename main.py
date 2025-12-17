from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scorebord import Score_bord
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score_bord()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food)<15:
        food.refresh()
        snake.new_body()
        score.increase()

    if snake.head.xcor()>290 or snake.head.xcor()<-300 or snake.head.ycor() >300 or snake.head.ycor() <-290:
        score.end()
        break
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.end()
            game_is_on=False








screen.exitonclick()