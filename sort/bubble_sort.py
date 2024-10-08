import random
import time

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


# x = list(range(1000))
# x.reverse()
# # random.shuffle(x)
# bubble_sort_debug(x)
# # print(x)


x = list(range(4500))
random.shuffle(x)
start_time = time.time()
bubble_sort(x)
end_time = time.time()
print(end_time - start_time)


x = list(range(3000000))
random.shuffle(x)
start_time = time.time()
x.sort()
end_time = time.time()
print(end_time - start_time)
