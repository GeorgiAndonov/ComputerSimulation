import numpy as np

class Polynomial:
    coefficients = []

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def print_order(self):
        for a in self.coefficients:
            if a != 0:
                ret = self.coefficients.index(a)
        print("The order of the polynomial is %d" % ret)

    def print_poly(self):
        if self.coefficients[0] != 0:
            print("P(x) = %.2f +" % self.coefficients[0], end=" ")
        else:
            print("P(x) =", end=" ")

        i = 1 # this is used for indexing
        for a in self.coefficients[1:len(self.coefficients) - 1]:
            if a != 0:
                print("%.2fx^%d +" % (a, i), end=" ")
            i += 1

        print("%.2fx^%d" % (self.coefficients[-1], len(self.coefficients) - 1))

    def add_poly(self, add_pol1):

        new_coefficients = []
        if len(self.coefficients) < len(add_pol1.coefficients):
            length = len(self.coefficients)
            larger = 1
        elif len(self.coefficients) > len(add_pol1.coefficients):
            length = len(add_pol1.coefficients)
            larger = 0
        else:
            length = len(add_pol1.coefficients)

        for i in range(length):
            new_coefficients.append(self.coefficients[i] + add_pol1.coefficients[i]) # itertools zip_longest // try to make it simpler

        if len(self.coefficients) != len(add_pol1.coefficients):
            if larger:
                new_coefficients += add_pol1.coefficients[length:]
            else:
                new_coefficients += self.coefficients[length:]

        return Polynomial(new_coefficients)

    def add_poly2(self, add_pol1): # a simpler way to do the function
        if len(self.coefficients) < len(add_pol1.coefficients):
            new_coefficients = np.array(self.coefficients) + np.array(add_pol1.coefficients[:len(self.coefficients)])
            new_coefficients = list(new_coefficients) + add_pol1.coefficients[len(self.coefficients):]
        else:
            new_coefficients = np.array(add_pol1.coefficients) + np.array(self.coefficients[:len(add_pol1.coefficients)])
            new_coefficients = list(new_coefficients) + self.coefficients[len(add_pol1.coefficients):]
        return Polynomial(new_coefficients)

    def differentiate_poly(self):
        diff_coeff = []
        for a in self.coefficients[1:]:
            diff_coeff.append(a*self.coefficients.index(a))

        return Polynomial(diff_coeff)

    def integrate_poly(self, c):
        integr_coeff = [c] # 2 is hardcoded as a coefficient c as said
        for a in self.coefficients:
            integr_coeff.append(a/(self.coefficients.index(a) + 1))

        return Polynomial(integr_coeff)
