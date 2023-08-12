from turtle import Turtle

# Constants for scoreboard display
POSITION = (0, 270)  # Position for displaying the score
ALIGNMENT = "center"  # Text alignment for score display
FONT = ("Courier", 20, "normal")  # Font style for score display

# Scoreboard class inherits from Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        # Initialize scoreboard properties
        self.score = 0  # Player's current score
        self.high_score = None  # Highest score recorded
        self.open_highscore()  # Read the high score from a file
        self.color("white")
        self.goto(POSITION)
        self.penup()
        self.hideturtle()
        self.update_score()  # Display initial score and high score

    # Open the high score from a file
    def open_highscore(self):
        with open("data.txt", mode="r") as highscore_txt:
            self.high_score = int(highscore_txt.read())

    # Save the new high score to a file
    def save_highscore(self, new_score):
        with open("data.txt", mode="w") as highscore_txt:
            highscore_txt.write(new_score)

    # Update and display the current score and high score
    def update_score(self):
        self.clear()  # Clear previous score display
        self.write(arg=f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    # Increase the player's score by 1 and update the display
    def increase_score(self):
        self.score += 1  # Increment the player's score
        self.update_score()  # Update the score display

    # Handle game over: update high score if necessary, reset score, and update display
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score  # Update high score if current score is higher
            self.save_highscore(new_score=str(self.high_score))  # Save the new high score to a file
        self.score = 0  # Reset the player's score
        self.update_score()  # Update the score display
