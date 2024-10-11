import random
import time

def insertion_sort(x):
    for i in range(1, len(x)):
        current = x[i]
        j = i - 1
        while j >= 0 and current < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = current


def insertion_sort_debug(x):
    assign = 0
    reads = 0
    for i in range(1, len(x)):
        current = x[i]
        reads += 1
        j = i - 1
        while j >= 0 and current < x[j]:
            reads += 1
            x[j + 1] = x[j]
            assign += 1
            j -= 1
        reads += 1
        x[j + 1] = current
        assign += 1
    print(reads, assign)


x = list(range(1000))
random.shuffle(x)
insertion_sort_debug(x)
# print(x)


x = list(range(6000))
random.shuffle(x)
start_time = time.time()
insertion_sort(x)
end_time = time.time()
print(end_time - start_time)
