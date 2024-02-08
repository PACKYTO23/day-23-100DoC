from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10


class CarManager(Turtle):
    """Lists of cars."""
    def __init__(self):
        self.start_move_distance = 2.5
        self.move_increment = 2.5
        self.all_cars = []

    def create_car(self):
        """Models initial car body and appends to car list."""
        random_chance = randint(1, 5)
        if random_chance == 5:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-235, 235)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        """Moves car left."""
        for car in self.all_cars:
            car.backward(self.start_move_distance)

    def increase_speed(self):
        """Increase cars' speed."""
        self.start_move_distance += 5
        for car in self.all_cars:
            car.backward(self.start_move_distance)
