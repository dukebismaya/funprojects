from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADINGS = {'Up': 90, 'Down': 270, 'Left': 180, 'Right': 0}

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != HEADINGS['Down']:
            self.head.setheading(HEADINGS['Up'])

    def down(self):
        if self.head.heading() != HEADINGS['Up']:
            self.head.setheading(HEADINGS['Down'])

    def left(self):
        if self.head.heading() != HEADINGS['Right']:
            self.head.setheading(HEADINGS['Left'])

    def right(self):
        if self.head.heading() != HEADINGS['Left']:
            self.head.setheading(HEADINGS['Right'])

    def extend(self):
        """Add a new segment at the current tail position."""
        tail = self.segments[-1]
        position = tail.position()
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
        