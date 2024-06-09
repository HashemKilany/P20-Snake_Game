from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", "r") as h:
            self.high_score = int(h.read())
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score : {self.score} - High score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as h:
                h.write(str(self.high_score))

        self.update_score()
