import matplotlib.pyplot as plt
import json, math

dic = json.load(open('entropy_efficiency.json', 'r'))

for i in range(1000):
    key = dic[str(i)]
    if key[1] == 'Too big':
        plt.plot(key[0], math.log2(16)/math.log2(i), 'r.')
    elif key[1] <= 0:
        plt.plot(key[0], 0, 'b.')
    else:
        plt.plot(key[0], math.log2(key[1])/math.log2(i), 'b.')

plt.ylim(-1, 1)
plt.show()