import matplotlib.pyplot as plt
import numpy as np
import math
import random
import pandas as pd

noise_scalar = 2.2
def mean(a):
    return sum(a) / len(a)
def deviation_between_lists(a,b):
    a1 = a.copy()
    b1 = b.copy()
    if len(a1) < len(b1):
        size_dif = len(b1) - len(a1)
        for x in range(size_dif):
            b1.pop(0)
    if len(a1) > len(b1):
        size_dif =  len(a1) - len(b1)
        for x in range(size_dif):
            a1.pop(0)
    error = 0
    for i in range(len(a1)):
        error += abs(a1[i] - b1[i])
    return abs(error / len(a1))

def moving_average(a, n=10):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return list(ret[n - 1:] / n)
def average_signal(a,b):
    c = []
    for i in range(len(a)):
        c.append(( (a[i] + b[i]) / 2) + 0)
    return c
plt.style.use("ggplot")

perfect_signal = [math.log(i + 1)  for i in range(100)]
noisy_signal = [(random.random() *2 ) * x for x in perfect_signal]
noisy_signal1 = [(random.random() *2) * y for y in perfect_signal]
moving_average_and_2_sensor = moving_average(average_signal(noisy_signal,noisy_signal1),1)
ma_windows = 1
for i in range(2,100):
    new_moving_average_and_2_sensor = moving_average(average_signal(noisy_signal,noisy_signal1),i)
    new_deviation = deviation_between_lists(perfect_signal,new_moving_average_and_2_sensor)
    previous_deviaton = deviation_between_lists(perfect_signal,moving_average_and_2_sensor)
    print (f"new: {new_deviation} old: {previous_deviaton}")
    if (new_deviation < previous_deviaton):
        print(f"new deviation is: {new_deviation}")
        print(f"i = {i}")
        ma_windows = i
        moving_average_and_2_sensor = new_moving_average_and_2_sensor


moving_average_and_2_sensor = moving_average(average_signal(noisy_signal,noisy_signal1),ma_windows)
moving_average_only = moving_average(noisy_signal)
ma2sensor = deviation_between_lists(perfect_signal,moving_average_and_2_sensor)
ma_only = deviation_between_lists(perfect_signal,moving_average_only)
print(f"deviation of moving_average_and_2_sensor is {ma2sensor}")
print(f"deviation of moving_average_only is {ma_only}")
if (ma2sensor < ma_only):
    print("moving average and dual sensors is superior!")
else:
    print("moving average and dual sensors is worse!")
print(f"moving average windows selected by optimizer = {ma_windows}")
plt.plot([mean(moving_average_and_2_sensor) for i in range(len(perfect_signal) - len(moving_average_and_2_sensor))] + moving_average_and_2_sensor,label="cute filter owo ")

plt.plot(perfect_signal,label="true signal ")
plt.plot(noisy_signal,label = "dumb bad measured signal")

#plt.plot(moving_average_only,label="ma only")
plt.legend()
plt.show()
