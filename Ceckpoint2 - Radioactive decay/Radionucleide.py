import numpy as np
import math as math


# Nucleide class containing the necessary attributes
class Radionucleide:
    def __init__(self, name, half_life):
        self.name = name
        self.decay = 0  # this is used to check if the atom is decayed (0 - not decayed / 1 - decayed)
        self.half_life = half_life
        self.decay_const = math.log(2) / self.half_life
