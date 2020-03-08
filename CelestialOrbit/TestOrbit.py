import numpy as np
import matplotlib.pyplot as plt
from SystemSimulator import OrbitalSystem


def main():
    # Testing the code
    sys = OrbitalSystem()
    sys.run()

    # Plotting the results from the KE
    fig = plt.figure()
    ax = plt.axes()
    x = np.array(sys.KE)
    # Adjusting the KE to smaller values
    x = x/(10**22)
    ax.set_xlim(0, len(sys.KE) - 1)
    ax.set_ylim(0, int(np.amax(x))*3)

    plt.plot(x)
    plt.show()


main()
