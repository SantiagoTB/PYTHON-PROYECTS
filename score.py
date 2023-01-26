from turtle import Turtle
x_position = 0
y_position = 280
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setpos(x_position,y_position)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}",align="center",font=("Arial",12,"normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def collision(self):
        self.setpos(0, 0)
        self.write("Game over", align="center", font=("Arial", 20, "normal"))






