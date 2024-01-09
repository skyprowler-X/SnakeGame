from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.goto(0, 260)
        self.color("White")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score = {self.score}  High score = {self.high_score}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.hideturtle()
        self.write("GAME OVER", align="center", font=("Courier", 50, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"score.txt", "w", encoding="UTF-8") as f:
                line = f"score: {self.score}"
                f.write(line)

        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        high_score = 0
        with open(r"score.txt", "r", encoding="UTF-8") as f:
            for line in f:
                if "score" in line:
                    line = line.split(":")[1].strip()
                    high_score = int(line)
        self.high_score = int(high_score)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
