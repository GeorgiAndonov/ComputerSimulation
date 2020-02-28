import numpy as np


class Road:
    def __init__(self):
        self.number_of_cells = int(input("Enter a value for the number of road cells: "))
        self.number_of_cars = int(input("Enter a value for the number of cars: "))
        self.road = np.zeros(self.number_of_cells)
        self.iterations = int(input("Enter a value for the number of iterations: "))
        self.road_iter = []
        self.average_speed = 0

    def initialise_cars(self):
        o = np.ones(self.number_of_cars, dtype=int)
        z = np.zeros(self.number_of_cells - self.number_of_cars, dtype=int)
        self.road = np.concatenate([o, z])
        np.random.shuffle(self.road)

    def move(self):
        for i in range(self.iterations):
            temp = np.copy(self.road)
            self.road_iter.append(temp)
            for j in range(len(self.road)):
                if self.road[j] == 1:
                    if j == len(self.road) - 1:
                        if self.road[0] == 1:
                            temp[j] = 1
                        else:
                            temp[j] = 0
                            temp[0] = 1
                    else:
                        if self.road[j + 1] == 1:
                            temp[j] = 1
                        else:
                            temp[j] = 0
                else:
                    if self.road[j - 1] == 1:
                        temp[j] = 1
                    else:
                        temp[j] = 0
            moving_cars = int(sum(1 for x, y in zip(self.road, temp) if x != y) / 2)
            self.road = np.copy(temp)
            self.average_speed = moving_cars/self.number_of_cars

