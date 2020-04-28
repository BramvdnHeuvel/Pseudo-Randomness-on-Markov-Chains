import random, math

def binary_len(num):
    i = 1
    n = 1
    while n <= num:
        i, n = i + 1, n * 2
    return i - 1

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

    for i in range(max_value):
        random.seed(encode(i))

        if seed_produces(good_word):
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

def seed_produces(word):
    numbers = {
        '0': {
            'switch': [],
            'stay': []
        },
        '1': {
            'switch': [],
            'stay': []
        }
    }

    for i in range(1, len(word)-1):
        a, b = word[i-1], word[i]

        if a == b:
            numbers[a]['stay'].append(random.random())
        else:
            numbers[a]['switch'].append(random.random())
    
    return is_disjoint(numbers['0']) and is_disjoint(numbers['1'])

def is_disjoint(dic):
    if len(dic['switch']) * len(dic['stay']) == 0:
        return True

    min_set_one, max_set_one = min(dic['switch']), max(dic['switch'])
    min_set_two, max_set_two = min(dic['stay']), max(dic['stay'])

    if min_set_one == min_set_two:
        return False
    
    if min_set_one < min_set_two:
        return max_set_one < min_set_two
    else:
        return max_set_two < min_set_one
