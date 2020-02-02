from encode import find_seed_for_value
from markov import MarkovChain
import random, json

dic = {}

for i in range(1000):
    if i % 100 == 0:
        print(f"Finding a seed for value {i}...")

    try:
        attempt = find_seed_for_value(i)
    except OverflowError:
        dic[i] = "Too big"
    else:
        dic[i] = attempt["fittingSeed"]["value"]

json.dump(dic, open('efficiency.json', 'w'))