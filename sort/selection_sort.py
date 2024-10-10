import random

def selection_sort(x):
    for i in range(len(x) - 1, 0, - 1):
        maximum = x[0]
        j_maximum = 0
        for j in range(1, i + 1):
            if x[j] > maximum:
                maximum = x[j]
                j_maximum = j
        x[j_maximum], x[i] = x[i], x[j_maximum]


def selection_sort_debug(x):
    swaps = 0
    reads = 0
    for i in range(len(x) - 1, 0, - 1):
        maximum = x[0]
        j_maximum = 0
        reads += 1
        for j in range(1, i + 1):
            reads += 1
            if x[j] > maximum:
                maximum = x[j]
                j_maximum = j
        x[j_maximum], x[i] = x[i], x[j_maximum]
        swaps += 1
    print(reads, swaps)


x = list(range(1000))
random.shuffle(x)
selection_sort_debug(x)
# print(x)
