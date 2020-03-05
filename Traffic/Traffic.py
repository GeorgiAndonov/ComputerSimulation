import numpy as np


# A class for the road
class Road:
    def __init__(self):
        self.number_of_cells = int(input("Enter a value for the number of road cells: "))
        self.number_of_cars = int(input("Enter a value for the number of cars: "))
        self.road = np.zeros(self.number_of_cells)
        self.iterations = int(input("Enter a value for the number of iterations: "))
        self.road_iter = []  # Contains the state of the road at each iteration
        self.average_speed = 0

    # Helper function to randomly place the cards on the road
    def initialise_cars(self):
        o = np.ones(self.number_of_cars, dtype=int)
        z = np.zeros(self.number_of_cells - self.number_of_cars, dtype=int)
        self.road = np.concatenate([o, z])
        np.random.shuffle(self.road)

    # Movement function
    def move(self):
        for i in range(self.iterations):
            # A copy of the current road condition where we change the values based on the values
            temp = np.copy(self.road)
            # Add the previous iteration to the iterations array
            self.road_iter.append(temp)
            # Compute the next iteration using temp
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
            # Calculating the total number of moving cars - it is the difference in characters in 2 adjacent iterations
            # divided by 2, as when 1 car moves it creates 2 differences
            moving_cars = int(sum(1 for x, y in zip(self.road, temp) if x != y) / 2)
            # Assign the newly calculated road as the new current condition
            self.road = np.copy(temp)
            # Calculate the average speed for plotting later
            self.average_speed = moving_cars/self.number_of_cars

