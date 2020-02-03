from markov import MarkovChain
import random, math

def entropy(num):
    """
        Calculate the entropy of a given integer.
    """
    dic = {'0': 0, '1': 0, 'total': 0}
    for char in encode(num):
        if char in ['1', '0']:
            dic[char] += 1
            dic['total'] += 1
    p0, p1 = dic['0']/dic['total'], dic['1']/dic['total']

    S = 0
    if p0 > 0:
        S = S - p0 * math.log2(p0)
    if p1 > 0:
        S = S - p1 * math.log2(p1)
    return S

def find_seed_for_value(num, max_value=1000000, raw=False):
    if not raw:
        good_word = encode(num)
        if num > 0:
            max_value = min(num*16, max_value)
    else:
        good_word = num

    m = MarkovChain()
    m.load(good_word)

    for i in range(max_value):
        random.seed(encode(i))
        word = m.get_name()

        if word == good_word:
            return {
                "fittingSeed": {
                    "value": i,
                    "seed": encode(i),
                    "length": len(encode(i))-1
                },
                "originalInput": {
                    "value": num,
                    "seed": good_word,
                    "length": len(good_word)-1
                }
            }
        elif i % 100000 == 0:
            if i > 0:
                print(f"Considered option {i} for value {num}...")
    else:
        raise OverflowError(f"Could not find a fitting seed under value {max_value}.")

def encode(num):
    """
        Convert an integer to a string containing the byte value.
    """
    if num <= 0:
        return '0\n'
    val = ''
    i = 1
    while i <= num:
        i *= 2
    
    while i > 0:
        i = i // 2

        if i == 0:
            return val + '\n'
        elif i <= num:
            val += '1'
            num = num - i
        else:
            val += '0'
