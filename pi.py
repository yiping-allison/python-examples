# This program will use the Monte Carlo vers of estimating Pi
# Author: Yiping (Allison)
# December 2017

import random

def generate_x_y_val():
    random_val = random.uniform(-1, 1)
    return random_val

def probability_in_circle(num_iterations):
    #count loop for probability in circle
    num_in_circle = 0
    for point in range(num_iterations):
        x_val = generate_x_y_val()
        y_val = generate_x_y_val()
        if x_val**2 + y_val**2 == 1:
            num_in_circle += 1
        elif x_val**2 + y_val**2 < 1:
            num_in_circle += 1
    return num_in_circle / num_iterations

def main():
    seed = int(input('Enter the seed for the random number generator: '))
    random.seed(seed)
    num_iterations = int(input('Enter the number of iterations to run: '))

    pi = probability_in_circle(num_iterations) * 4
    print('The value of pi is %.3f.' % pi)

main()
