from turtle import Turtle
STARTIGN_POSITION=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

# crearte a snake body
    def create_snake(self):
        for position in STARTIGN_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.shapesize(1,1)
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    def new_body(self):
        body=Turtle("square")
        body.color("white")
        body.shapesize(1, 1)
        body.penup()
        body_x=self.segments[len(self.segments)-1].xcor()
        body_y =self.segments[len(self.segments)-1].ycor()
        body.goto(body_x,body_y)
        self.segments.append(body)

#make a movement in my snake
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(7000,7000)
        self.segments.clear()

        self.create_snake()
        self.head = self.segments[0]

# changing_direction
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

