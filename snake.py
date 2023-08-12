from turtle import Turtle
import random

# Constants for snake movement and appearance
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for snake segments
MOVE_DISTANCE = 20  # Distance the snake moves in each step
UP = 90  # Heading for moving up
DOWN = 270  # Heading for moving down
RIGHT = 0  # Heading for moving right
LEFT = 180  # Heading for moving left
COLORS = ["#f5f4e8", "#c50d66", "#f07810", "#eec60a", "#57D1C9", "#ED5485", "#FFFBCB", "#FFE869"]  # Snake segment colors

# Snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.starting_positions = STARTING_POSITIONS
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The first segment is the head of the snake

    # Create the initial snake by adding segments at starting positions
    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    # Add a new segment to the snake
    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color(random.choice(COLORS))  # Randomly choose a color for the segment
        segment.goto(position)
        self.segments.append(segment)

    # Move the snake by updating the positions of its segments
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=x, y=y)
        self.head.forward(MOVE_DISTANCE)

    # Increase the length of the snake by adding a new segment
    def grow(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    # Reset the snake's position and segments
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move the segment off-screen
        self.segments.clear()  # Clear the segments list
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]  # Update the snake's head reference

    # Change the snake's direction to up
    def up(self):
        if self.head.heading() != DOWN:  # Prevent reversing direction
            self.head.setheading(UP)

    # Change the snake's direction to down
    def down(self):
        if self.head.heading() != UP:  # Prevent reversing direction
            self.head.setheading(DOWN)

    # Change the snake's direction to right
    def right(self):
        if self.head.heading() != LEFT:  # Prevent reversing direction
            self.head.setheading(RIGHT)

    # Change the snake's direction to left
    def left(self):
        if self.head.heading() != RIGHT:  # Prevent reversing direction
            self.head.setheading(LEFT)
