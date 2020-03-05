import matplotlib.pyplot as plt


class TrafficPlot:
    def __init__(self, nIter, road):
        self.road = road  # It is an instance of the class Road
        self.nIter = nIter  # Number of iterations
        self.all_iter = self.road.road_iter  # All road conditions calculated
        self.circles = []  # An array for the patches - circles

    def fill_circles(self):
        y = 1  # y-coordinate
        for sub in self.all_iter:
            p = []
            x = 1  # x-coordinate start
            for num in sub:
                if num == 1:
                    circle = plt.Circle((x, y), 0.3, color="red")
                    p.append(circle)
                else:
                    circle = plt.Circle((x, y), 0.3, facecolor="white", edgecolor='k')
                    p.append(circle)
                x += 2  # change the x-coordinate for the next circle - when we have x += 2 it looks better on the plot
            y += 1  # change the y-coordinate for the next iteration of the road
            self.circles.append(p)  # Fill the circles
