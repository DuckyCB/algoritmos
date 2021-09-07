import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import progressbar


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


cantidad = 2000

n = list(range(0, cantidad))
t = []

bar_progres = 0
bar_positive = progressbar.ProgressBar(max_value=cantidad)
bar_positive.update(bar_progres)

for size in range(cantidad):
    arr_ran = np.random.randint(0, 100, size=size)
    start = datetime.now()
    selection_sort(arr_ran)
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
