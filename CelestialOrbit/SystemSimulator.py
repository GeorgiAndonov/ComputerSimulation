import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Celestial import Celestial

GRAVITATIONAL_CONSTANT = 6.67408e-11


class OrbitalSystem(object):

    def __init__(self):
        self.celestials = []  # Container to store all of the celestials in a system
        mars = Celestial(500, "Mars")
        self.celestials.append(mars)
        phobos = Celestial(500, "Phobos")
        self.celestials.append(phobos)
        deimos = Celestial(500, "Deimos")
        self.celestials.append(deimos)
        data = np.array_split(np.loadtxt("test.txt"), len(self.celestials))  # Reading the data from a file

        # Filling the information retrieved from the file into the objects
        for i in range(len(self.celestials)):
            self.celestials[i].mass = data[i][0]
            self.celestials[i].pos[0] = data[i][1]
            self.celestials[i].pos[1] = data[i][2]
            self.celestials[i].velocity[0] = data[i][3]
            self.celestials[i].velocity[1] = data[i][4]

        # Setting the initial velocity of the moons
        phobos.set_initial_velocity(mars)
        deimos.set_initial_velocity(mars)
        self.KE = []  # Container for the kinetic energy at the specified timestamps
        self.patches = []
        self.iterations = 2400  # Number of iterations
        self.colours = ['red', 'grey', 'lightgrey']  # Colours for my circles

    # Init function for the animation
    def init(self):
        return self.patches

    # The start function
    def run(self):
        fig = plt.figure()
        ax = plt.axes()
        for i, cel in enumerate(self.celestials, 0):
            if i == 0:  # This is to make Mars larger than the moons
                self.patches.append(plt.Circle(cel.pos, 25e5, color=self.colours[i], animated=True))
            else:
                self.patches.append(plt.Circle(cel.pos, 7e5, color=self.colours[i], animated=True))

        # Adding the patches to the plot
        for patch in self.patches:
            ax.add_patch(patch)

        # Setting the boundaries and scaling the axis in order to have a better animation
        ax.axis('scaled')
        ax.set_xlim(-30e06, 30e06)
        ax.set_ylim(-30e06, 30e06)
        # Setting the background colour to black - space
        ax.patch.set_facecolor('black')

        # Creating the animation
        anim = FuncAnimation(fig, self.animate, init_func=self.init, frames=self.iterations, repeat=False,
                             interval=40, blit=True)
        plt.show()

    # Animation function
    def animate(self, i):
        # Update the values of each celestial
        for cel in self.celestials:
            cel.compute_force(self.celestials)
            cel.compute_acceleration()
            cel.compute_velocity()
            cel.compute_position()

        # Adjust the centres of the patches
        for j in range(0, len(self.patches)):
            self.patches[j].center = self.celestials[j].pos

        # The timestamp for KE
        if i % 20 == 0:
            self.compute_KE()

        return self.patches

    # Computing the kinetic energy of the system at a given timestamp and storing the value in KE
    def compute_KE(self):
        k_en = 0
        for cel in self.celestials:
            k_en += 0.5*cel.mass*(np.linalg.norm(cel.velocity)**2)
        self.KE.append(k_en)
        print(k_en)
