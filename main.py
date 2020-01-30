from markov import MarkovChain
import random

# Bouw de Markovketen
m = MarkovChain()
m.load('names.txt')

# random.seed(5)

for _ in range(10):
    m.print_name()

m.save()
