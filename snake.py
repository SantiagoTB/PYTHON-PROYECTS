from turtle import Turtle
move_distance = 20
positions = [(0,0),(-20,0),(-40,0)]
up = 90
down = 270
left = 180
right = 0

class Snake:

    def __init__(self):
        self.bloques = []
        self.create_snakes()
        self.head = self.bloques[0]

    def create_snakes(self):
        for pos in positions:
            self.add_block(pos)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def move(self):
        for block in range(len(self.bloques) - 1, 0, -1):
            pos_x = self.bloques[block - 1].xcor()
            pos_y = self.bloques[block - 1].ycor()
            self.bloques[block].goto(pos_x, pos_y)
        self.bloques[0].forward(move_distance)

    def add_block(self,position):
        block = Turtle(shape="square")
        block.color("white")
        block.penup()
        block.setpos(position)
        self.bloques.append(block)

    def increase_tail(self):
      self.add_block(self.bloques[-1].position())


