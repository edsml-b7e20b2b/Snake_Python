import time
from snake import Snake
from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     measuring distance to food

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()




#     collosion with wall

    if -290 > snake.head.xcor() or snake.head.xcor() > 290 or -290> snake.head.ycor() or snake.head.ycor() > 290:
        # game_is_on =False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()


# Collision with tail

    for segment in snake.snake_body:
        if snake.head.distance(segment) == 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()









screen.exitonclick()