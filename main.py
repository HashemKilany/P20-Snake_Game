from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)


def play_snake():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) <= 15:
            food.new_food()
            snake.extend()
            scoreboard.score_increase()

            # Detect collision with tail
        for segment in snake.snake[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()

        # detect collision with wall
        if (
                snake.head.xcor() < -280
                or snake.head.xcor() > 280
                or snake.head.ycor() < -280
                or snake.head.ycor() > 280
        ):
            game_on = False
            scoreboard.game_over()

            play_again = screen.textinput("Game Over!", "Do you want to play again? (yes/no)").lower()

            if play_again == "yes":
                screen.reset()
                # food = Food()
                # scoreboard = Scoreboard()
                # snake = Snake()
                play_snake()
            else:
                screen.bye()


play_snake()
screen.exitonclick()
