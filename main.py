from encode import find_seed_for_value, entropy
from markov import MarkovChain
import random, json

def convert_number_to_efficiency():
    """
        Given the values in `efficiency.json`, make a list that maps the numbers to the given entropy.
    """
    dic = json.load(open('efficiency.json', 'r'))
    new_dic = {}
    i = 1
    new_dic[0] = (entropy(0), dic['0'])

    while str(i) in dic:
        if dic[str(i)] != 'Too big':
            new_dic[i] = (entropy(i), dic[str(i)]/i)
        else:
            new_dic[i] = (entropy(i), "Too big")
        i += 1
    json.dump(new_dic, open('entropy_efficiency.json', 'w'))

def search_for_more_values():
    """
        Look for the most efficient seed that reproduces the given number.
        Found values are stored in `efficiency.json` when the user interrupts the function.
    """
    dic = json.load(open('efficiency.json', 'r'))

    try:
        for i in range(100000):
            if str(i) in dic:
                if i % 500 == 0:
                    print(f"Skipping value {i}...")
                continue

            if i % 10 == 0:
                print(f"Finding a seed for value {i}...")

            try:
                attempt = find_seed_for_value(i)
            except OverflowError:
                dic[i] = "Too big"
            else:
                dic[i] = attempt["fittingSeed"]["value"]
        else:
            raise KeyboardInterrupt()
    except KeyboardInterrupt:
        json.dump(dic, open('efficiency.json', 'w'))

if __name__ == '__main__':
    convert_number_to_efficiency()