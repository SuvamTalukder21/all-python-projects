import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# Set up the screen
window = Screen()
window.title("Turtle Crossing Game")
window.setup(width=600, height=600)
window.tracer(0)

# Create the player 'turtle'
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Keyboard bindings
window.listen()
window.onkeypress(fun=player.move_up, key="Up")
window.onkeypress(fun=player.move_down, key="Down")

# Set the initial state of the game
game_over = False

# Start the game loop
while not game_over:
    time.sleep(0.1)
    window.update()

    car_manager.create_car()  # Create the cars
    car_manager.move_car()  # Move the turtle

    # Check if the turtle has collided with a car
    for cars in car_manager.all_cars:
        if cars.distance(player) < 23:
            scoreboard.game_over()
            game_over = True

    # Check if the turtle has reached the other side of the road
    if player.finish_line():
        player.starting_position()
        car_manager.level_up()
        scoreboard.increase_level()

    if car_manager.car_speed == 20:
        game_over = True

# Close the game window when the game ends
window.exitonclick()
