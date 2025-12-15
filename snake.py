from turtle import Turtle
STARTIGN_POSITION=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIHGT=0

class Snake:
    def __int__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

# crearte a snake body
    def create_snake(self):
        for position in STARTIGN_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

#make a movement in my snake
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(DISTANCE)
# changing_direction
    def up(self):
        if self.head.setheading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.setheading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.setheading() != RIHGT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.setheading() != LEFT:
            self.head.setheading(RIHGT)

