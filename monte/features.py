from math import sqrt, pi
from random import uniform


class carlo:
    square_side = 0
    radius_circle = 0
    total = 0

    # # functions
    def get_number(self, for_: str):
        while True:
            try:
                number = int(input(f"Enter number for {for_} : "))
                if number >= 1:
                    return number
                else:
                    print("Enter number greater or equals to 1 ... ")
            except ValueError:
                print("Invalid number ... ")

    # methods
    def __init__(self):
        self.square_side = self.get_number("square side")
        self.radius_circle = self.square_side / 2
        self.total = self.get_number("number of test")

    def pi_estimate(self):

        # make dots
        dots = []
        for _ in range(self.total):
            rnd_range = self.square_side / 2

            x = uniform(-rnd_range, rnd_range)
            y = uniform(-rnd_range, rnd_range)

            distance = sqrt(x**2 + y**2)

            if distance <= self.radius_circle:
                dots.append(True)
            else:
                dots.append(False)

        # Results
        inside_circle = dots.count(True)
        outside_circle = dots.count(False)

        experimental_probability = inside_circle / self.total * 100

        theoretical_probability = (
            pi * self.radius_circle**2 / self.square_side**2
        ) * 100

        estimated_pi = 4 * experimental_probability

        absolute_error = abs(estimated_pi - pi)

        relative_error = (absolute_error / pi) * 100

        # Output
        print()
        print("=" * 50)
        print("             Monte Carlo Pi Estimation")
        print("=" * 50)

        print()
        print("Configuration")
        print("-" * 50)
        print(f"Square side              : {self.square_side}")
        print(f"Circle radius            : {self.radius_circle}")
        print(f"Number of simulations    : {self.total:,}")

        print()
        print("Results")
        print("-" * 50)
        print(f"Points inside circle     : {inside_circle:,}")
        print(f"Points outside circle    : {outside_circle:,}")

        print(f"Experimental probability : {experimental_probability:.5f}%")
        print(f"Theoretical probability  : {theoretical_probability:.5f}%")

        print()
        print("=" * 50)
