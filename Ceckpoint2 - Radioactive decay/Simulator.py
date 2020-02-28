import random as ran
import numpy as np
import math as math
from Radionucleide import Radionucleide


# Simulator class to conduct the experiment, containing the necessary environment variables
class Simulator:
    def __init__(self):
        self.num_atoms = int(input("Enter a value for the number of atoms: "))  # Number of atoms in a single row
        self.total_num = self.num_atoms * self.num_atoms
        self.num_decayed = 0
        # create a 2D array of size [num_atoms][num_atoms]
        self.atoms = np.array(
            [[Radionucleide("Iodine-128", 24.98) for _ in range(self.num_atoms)] for _ in range(self.num_atoms)])
        self.decay_const = float(input("Enter a value for the decay constant: "))
        self.timestamp = float(input("Enter timestamp: "))
        self.total_time = 0  # Here we store the total time to get T1/2
        self.probability = self.decay_const * self.timestamp

    def check_decay(self):

        while self.num_decayed < self.total_num / 2:
            for ix, iy in np.ndindex(self.atoms.shape):
                if not self.atoms[ix][iy].decay:
                    if ran.uniform(0, 1) < self.probability:  # Checking if the atom should be decayed
                        self.atoms[ix][iy].decay = 1
                        self.num_decayed += 1
            self.total_time += self.timestamp
        self.print_atoms()

    # Helper function to print the array with decayed/not decayed nuclei
    def print_atoms(self):
        decay_array = np.array([])  # creating an array to store the decays
        for ix, iy in np.ndindex(self.atoms.shape):
            decay_array = np.append(decay_array, self.atoms[ix][iy].decay)
        decay_array = decay_array.reshape(self.num_atoms, self.num_atoms)
        print(decay_array)
        print("Initial number of atoms: ", self.num_atoms * self.num_atoms)
        print("Total number of decayed atoms: ", self.num_decayed)
        print("T1/2 simulated = %f" % self.total_time)
        print("T1/2 original = %f" % self.atoms[0][0].half_life)
        # The absolute value of the difference between the calculated and the expected value
        print("Uncertainty: %f" % abs(self.atoms[0][0].half_life - self.total_time))


def main():

    simul = Simulator()
    simul.check_decay()


main()
