from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initialize the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create the snake, food, and scoreboard objects
snake = Snake()
food = Food()
score_board = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

# Game loop
game_speed = 0.2
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen to display changes
    time.sleep(game_speed)  # Pause to control the speed of the game

    snake.move()  # Move the snake

    # Check if the snake has eaten the food
    if snake.head.distance(food) < 15:
        food.move()  # Move the food to a new position
        snake.grow()  # Grow the snake
        score_board.increase_score()  # Increase the player's score
        if game_speed > 0.1:
            game_speed -= 0.01  #increase game_speed

    # Check if the snake hits the wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        snake.reset()  # Reset the snake's position
        score_board.game_over()  # End the game
        game_speed = 0.2  #reset game speed

    # Check for collision with snake's own body segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()  # End the game and show game over message
            snake.reset()  # Reset the snake's position

# Exit the game when the screen is clicked
screen.exitonclick()
