from turtle import Turtle

X_COORDINATES = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]
        
    def create_snake(self):
        for block in X_COORDINATES:         
            self.add_block(block)
 
    def add_block(self, block):
        snake = Turtle(shape='square')
        snake.penup()
        snake.color('white')
        snake.goto(block)
        self.snake_blocks.append(snake)


    def extend(self):
        self.add_block(self.snake_blocks[-1].position())


    def move(self):
        for block_num in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[block_num - 1].xcor()
            new_y = self.snake_blocks[block_num - 1].ycor()
            self.snake_blocks[block_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def reset(self):
        for blocks in self.snake_blocks:
            blocks.goto(900, 900)
        self.snake_blocks.clear()
        self.create_snake()
        self.head = self.snake_blocks[0]


    def up(self):
        if self.head.heading() != 270:  
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:  
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:  
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:  
            self.head.setheading(180)

  


