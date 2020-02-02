import matplotlib.pyplot as plt
import json

dic = json.load(open('efficiency.json', 'r'))

for i in range(1000):
    key = dic[str(i)]
    if key == 'Too big':
        plt.plot(i, 0, 'r.')
    else:
        plt.plot(i, key, 'b.')

plt.show()