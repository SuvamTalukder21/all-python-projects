import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)  # Face upward
        self.starting_position()

    def starting_position(self):
        self.goto(STARTING_POSITION)

    # Function to move the turtle up
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # Function to move the turtle down
    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
