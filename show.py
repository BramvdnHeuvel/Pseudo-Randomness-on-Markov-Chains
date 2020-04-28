import matplotlib.pyplot as plt
import json, math
from encode import binary_len

dic = json.load(open('efficiency.json', 'r'))

for i in range(40000):
    key = dic[str(i)]
    if key == 'Too big':
        plt.plot(i, 4.5, 'r.')
    elif key * i == 0:
        plt.plot(i, -1*binary_len(i), 'g.')
    else:
        plt.plot(i, binary_len(key) - binary_len(i), 'b.')
    
    if i % 1000 == 0:
        print(i)
else:
    plt.plot([0, i], [0, 0], 'y-')
    plt.plot(
        [0, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256, 256, 512, 512, 1024, 1024, 2048, 2048, 4096, 4096, 8192, 8192, 16384, 16384, 32768, 32768, 40000],
        [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9, -9, -10, -10, -11, -11, -12, -12, -13, -13, -14, -14, -15, -15, -16, -16],
        'y-'
    )

plt.show()