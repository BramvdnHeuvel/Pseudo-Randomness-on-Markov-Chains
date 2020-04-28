from scipy.special import binom
from matplotlib import pyplot as plt
import math

def max_expectation(n, k):
    l = math.log2(binom(n, k))

    i = int(l)

    return i + 1

def expectancy_list(n, scale=False):
    s = n if scale else 1

    return [max_expectation(n, k)/s for k in range(n+1)]

if __name__ == '__main__':
    plt.plot([0, 1], [1, 1], 'b-')

    plt.plot([i/1000 for i in range(1000 + 1)], expectancy_list(1000, scale=True), 'r.')
    plt.plot([i/100  for i in range( 100 + 1)], expectancy_list( 100, scale=True), 'g.')
    plt.plot([i/10   for i in range(  10 + 1)], expectancy_list(  10, scale=True), 'y.')

    plt.show()
