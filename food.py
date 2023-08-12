from turtle import Turtle
import random

# Food class inherits from Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()

        # Initialize food properties
        self.color("yellow")  # Set food color
        self.shape("circle")  # Set food shape
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Adjust food size
        self.speed("fastest")  # Set the animation speed to the fastest
        self.move()  # Move the food to a random position

    # Move the food to a random position on the screen
    def move(self):
        random_x = random.randint(-280, 280)  # Generate random x-coordinate
        random_y = random.randint(-280, 280)  # Generate random y-coordinate
        self.goto(x=random_x, y=random_y)  # Move the food to the generated position
