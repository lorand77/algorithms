import random

def bubble_sort(x):
    for i in range(len(x) - 1, 0, - 1):
        for j in range(0, i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


def bubble_sort_debug(x):
    swaps = 0
    reads = 0
    for i in range(len(x) - 1, 0, - 1):
        for j in range(0, i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                swaps += 1
            reads += 2
    print(reads, swaps)


x = list(range(1000))
x.reverse()
# random.shuffle(x)
bubble_sort_debug(x)
# print(x)
