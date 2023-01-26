from turtle import Screen
from score import Score
from snake import Snake
from food import Food
import time

screen = Screen()
screen.bgcolor("black")
screen.title(titlestring="snake game")
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
score = Score()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #score control
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.increase_tail()

    #collision with the wall control
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.collision()
        game_is_on = False

    #collision with tail control
    for block in snake.bloques[1:]:
        if snake.head.distance(block) < 10:
            score.collision()
            game_is_on = False

screen.exitonclick()
