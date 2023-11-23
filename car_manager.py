import random
import turtle

# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
COLORS = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []  # Create a list of cars
        self.car_speed = STARTING_MOVE_DISTANCE

    # Function to create a car
    def create_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 4:
            new_car = turtle.Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.y_position = random.randint(-250, 250)
            new_car.setposition(x=300, y=new_car.y_position)
            self.all_cars.append(new_car)

    # Move the cars
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
