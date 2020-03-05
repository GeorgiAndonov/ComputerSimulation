import numpy as np
import matplotlib.pyplot as plt
from Traffic import Road
from TrafficPlot import TrafficPlot


def plot_graph(road):
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


def main():
    road = Road()
    road.initialise_cars()
    road.move()

    plot = TrafficPlot(road.iterations, road)
    plot.fill_circles()

    fig = plt.figure()
    ax = plt.axes()

    for sub in plot.circles:
        for c in sub:
            ax.add_patch(c)

    ax.axis('scaled')
    ax.set_xlim(0, len(plot.circles[0]) * 2)
    ax.set_ylim(0, plot.nIter + 1)

    plt.xlabel("Cars")
    plt.ylabel("Iteration")
    plt.show()

    plot_graph(road)


main()

