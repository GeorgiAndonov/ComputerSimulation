import numpy as np


class Celestial(object):
    def __init__(self, dt, name):
        self.GRAVITATIONAL_CONSTANT = 6.67408e-11
        self.dt = dt  # Delta t - difference in time
        self.name = name
        self.__mass = 0
        self.pos = np.array([0, 0])
        self.velocity = np.array([0, 0])
        self.acceleration = np.array([0, 0])
        self.force = np.array([0, 0]) # The force on a celestial at a given time by all other objects in the system

    # A getter and a setter for the mass
    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, m):
        self.__mass = m

    # Helper function to set the initial velocity of the moons
    def set_initial_velocity(self, orb):  # orb in this case will be Mars
        self.velocity[1] = (self.GRAVITATIONAL_CONSTANT*orb.mass/(np.linalg.norm(self.pos - orb.pos)))**(1/2)

    def compute_position(self):
        self.pos = self.pos + self.velocity*self.dt

    def compute_velocity(self):
        self.velocity = self.velocity + self.dt*self.acceleration

    # Takes as an argument all celestials in a system
    def compute_force(self, arr_sys):
        self.force = 0
        for cel in arr_sys:
            if cel.name != self.name:  # I use the name of a celestial as an indicator
                # Helper variables to make the code look cleaner
                m = cel.mass*self.mass
                rpos = np.linalg.norm(cel.pos - self.pos)
                rpos_unit = (1/rpos)*(cel.pos - self.pos)
                self.force += (m/(rpos**2))*rpos_unit
        self.force = self.GRAVITATIONAL_CONSTANT*self.force

    def compute_acceleration(self):
        self.acceleration = self.force/self.mass
