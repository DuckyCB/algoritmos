import numpy as np
import matplotlib.pyplot as plt
import progressbar
import random
from datetime import datetime
import time


def binary_search(arr, element):
    pos_min = 0
    pos_max = len(arr) - 1
    while pos_min <= pos_max:
        pos_mid = (pos_min + pos_max) // 2

        if arr[pos_mid] > element:
            pos_max = pos_mid - 1
        elif arr[pos_mid] < element:
            pos_min = pos_mid + 1
        else:
            return pos_mid
    return -1


def find_min(elements, from_index, to_index):
    index_min = from_index
    for index in range(from_index, to_index):
        if elements[index] < elements[index_min]:
            index_min = index
    return index_min


def selection_sort(elements):
    for i in range(len(elements)):
        index = find_min(elements, i, len(elements))
        elements[i], elements[index] = elements[index], elements[i]


cantidad = 200

n = list(range(1, cantidad))
t = []

bar_progres = 0
bar_positive = progressbar.ProgressBar(max_value=cantidad)
bar_positive.update(bar_progres)

for size in range(1, cantidad):
    arr_ran = np.random.randint(0, 100 if size > 100 else size, size=size)
    start = datetime.now()
    number = random.choice(arr_ran)
    binary_search(arr_ran, number)
    time = datetime.now() - start
    t.append(time.microseconds)
    bar_progres += 1
    bar_positive.update(bar_progres)

t = np.array(t)
n = np.array(n)

plt.plot(n, t)
plt.ylabel('tiempo')
plt.xlabel('tamaño')
plt.show()
