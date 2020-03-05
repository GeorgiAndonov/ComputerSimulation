import numpy as np
import matplotlib.pyplot as plt
from Traffic import Road
from TrafficPlot import TrafficPlot


# Helper function to plot the graph of the average speed compared to the density
def plot_graph(road):
    x = np.linspace(0, 1, road.number_of_cells)  # creates an array filled with all of the possible densities
    y = []  # This will store the average speed

    # Calculate the average speed for each density
    for i in range(road.number_of_cells):
        road.number_of_cars = i + 1
        road.initialise_cars()
        road.move()

        y.append(road.average_speed)

    # Plot the function
    plt.plot(x, y)
    plt.xlabel("Density")
    plt.ylabel("Average Speed")
    plt.show()


# Helper function to plot the iterations
def plot_road_iter(plot):
    plot.fill_circles()
    fig = plt.figure()
    ax = plt.axes()

    # Adding the patches
    for sub in plot.circles:
        for c in sub:
            ax.add_patch(c)

    ax.axis('scaled')
    ax.set_xlim(0, len(plot.circles[0]) * 2)  # *2 here because I increment teh x by 2 each iteration
    ax.set_ylim(0, plot.nIter + 1)  # The max_y would be the number of iterations + 1 because we start from 0

    plt.xlabel("Cars")
    plt.ylabel("Iteration")
    plt.show()


def main():
    road = Road()
    road.initialise_cars()
    road.move()

    plot = TrafficPlot(road.iterations, road)
    plot_road_iter(plot)
    plot_graph(road)


main()

