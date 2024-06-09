from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_seg(position)

    def add_seg(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setpos(position)
        #segment.setpos(x, y)
        self.snake.append(segment)
        #x -= 20

    def extend(self):
        self.add_seg(self.snake[-1].position())

    def reset(self):
        self.snake = []
        self.create_snake()

    def move(self):
        for s in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[s - 1].xcor()
            new_y = self.snake[s - 1].ycor()
            self.snake[s].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
