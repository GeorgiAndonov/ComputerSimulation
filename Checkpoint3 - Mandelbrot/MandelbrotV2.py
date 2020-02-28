import numpy as np
import matplotlib.pyplot as plt


# This is a helper function that calculates the colour value (0 -> 255)
def mandelbrot_calc(Re, Im, end):
    C = complex(Re, Im)  # Create a complex number using: Re - real part / Im - imaginary part
    z = 0  # First iteration is always = 0

    for i in range(end):
        z = z * z + C  # Calculate the next z
        if (z.real * z.real + z.imag * z.imag) >= 4:  # Check if it diverges
            return i

    return end


# This is basically the resolution of the image
width = 1000
height = 1000

x = np.linspace(-2.025, 0.6, width)  # Creates an array containing the coordinate vector of the x-axis
y = np.linspace(-1.125, 1.125, height)  # Creates an array containing the coordinate vector of the y-axis

XX, YY = np.meshgrid(x, y)  # Creates 2D arrays for the corresponding coordinate vectors
m_func = np.vectorize(mandelbrot_calc)  # With this we can apply the function to each element of a numpy array
result = m_func(XX, YY, 255)  # This maps the function using each element of both arrays and stores the values

# Plotting the figure using the result 2D array
plt.figure(dpi=100)
plt.imshow(result)
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()