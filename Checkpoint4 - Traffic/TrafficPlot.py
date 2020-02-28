import matplotlib.pyplot as plt
from Traffic import Road


class TrafficPlot:
    def __init__(self, nIter, road):
        self.road = road
        self.nIter = nIter
        self.test_array = self.road.road_iter
        self.circles = []

    def fill_circles(self):
        y = 1
        for sub in self.test_array:
            p = []
            x = 1
            for num in sub:
                if num == 1:
                    circle = plt.Circle((x, y), 0.3, color="red")
                    p.append(circle)
                else:
                    circle = plt.Circle((x, y), 0.3, facecolor="white", edgecolor='k')
                    p.append(circle)
                x += 2
            y += 1
            self.circles.append(p)


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


main()
