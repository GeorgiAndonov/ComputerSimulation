import numpy as np
import matplotlib.pyplot as plt
from Traffic import Road


def main():
    road = Road()
    x = np.linspace(0, 1, road.number_of_cells)
    y = []

    for i in range(road.number_of_cells):
        road.number_of_cars = i + 1
        road.initialise_cars()
        road.move()

        y.append(road.average_speed)

    plt.plot(x, y)
    plt.xlabel("Density")
    plt.ylabel("Average Speed")
    plt.show()


main()
