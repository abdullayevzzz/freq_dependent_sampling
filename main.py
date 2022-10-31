import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
max_comp = 10

with open('01.csv') as f:
    orig = [float(line.strip('\r\n')) for line in f]

mean_orig = mean(orig)
orig = [elem - mean_orig for elem in orig]
plt.plot(orig)
plt.show()

dif = []
for i in range(1, len(orig)):
    dif.append(abs(orig[i] - orig[i - 1]))

max_dif = max(dif)
dif = [min(max_comp, int(max_dif / elem) if elem != 0 else max_comp) for elem in dif]
plt.plot(dif)
plt.show()

encoded = []
i = 0
while i < len(dif):
    encoded.append(orig[i])
    i = i + dif[i]

plt.plot(encoded)
plt.show()

decoded = []
i = 0
while i < len(encoded):
    decoded.append(encoded[i])
    for _ in range(i):
        i = i + dif[i]



