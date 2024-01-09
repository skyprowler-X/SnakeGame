import turtle as t

STARTING_POSITION =[(0,0),(-20, 0),(-40, 0)]
STARTING_MOVEMENT = 20
UP = 90
RIGHT =0
DOWN = 270
LEFT = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_number in range(len(self.snake) -1 , 0, -1):   
            new_xcor = self.snake[seg_number -1].xcor()
            new_ycor = self.snake[seg_number -1].ycor()
            self.snake[seg_number].goto(new_xcor,new_ycor)
        self.head.forward(STARTING_MOVEMENT)
        
    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self): 
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

