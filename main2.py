import matplotlib.pyplot as plt

MAX_COMP = 12  # maximum compression limit
MAX_CALIBRATION = 1

with open('01.csv') as f:
    orig = [float(line.strip('\r\n')) for line in f]
#mean_orig = mean(orig)
#orig = [elem - mean_orig for elem in orig]


dif_plot = []
time_period_plot = []
encoded = []
decoded = []


def map_range(value, in_min, in_max, out_min, out_max):
    return int(round((out_min + (((value - in_min) / (in_max - in_min)) * (out_max - out_min)))))


def encode(orig_sig):
    max_dif = 0
    i = 0
    while i < len(orig_sig) - 1:
        encoded.append(orig_sig[i])
        dif = (abs(orig_sig[i] - orig_sig[i + 1]))
        dif_plot.append(dif)
        if dif > max_dif:
            max_dif = dif
        if dif != 0:
            time_period = map_range(int(max_dif / dif), 0, max_dif, 1, MAX_COMP)
        else:
            time_period = MAX_COMP
        time_period_plot.append(time_period)
        i += time_period  # skip samples
        max_dif -= MAX_CALIBRATION  # to vanish old value, auto-calibrate over time


def decode(encoded_sig, time_period_sig):
    for i, item in enumerate(encoded_sig):
        for _ in range(time_period_sig[i]):
            decoded.append(item)


encode(orig)
decode(encoded, time_period_plot)

plt.figure(1, figsize=(6, 8))
plt.subplot(5, 1, 1)
plt.subplots_adjust(hspace=0.8)
plt.gca().set_title('Original')
plt.plot(orig)

plt.subplot(5, 1, 2)
plt.gca().set_title('Sampling frequency')
plt.plot(dif_plot)

plt.subplot(5, 1, 3)
plt.gca().set_title('Sampling period (normalized)')
plt.plot(time_period_plot)

plt.subplot(5, 1, 4)
plt.gca().set_title('Encoded')
plt.plot(encoded)

plt.subplot(5, 1, 5)
plt.gca().set_title('Decoded')
plt.plot(decoded)
plt.show()
