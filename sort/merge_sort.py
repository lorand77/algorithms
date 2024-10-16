import random
import time

def merge_sort(x):
    if len(x) > 1:
        m = len(x) // 2
        xl = x[:m]
        xr = x[m:]

        merge_sort(xl)
        merge_sort(xr)

        i = j = k = 0
        while i < len(xl) and j < len(xr):
            if xl[i] < xr[j]:
                x[k] = xl[i]
                i += 1
            else:
                x[k] = xr[j]
                j += 1
            k += 1

        while i < len(xl):
            x[k] = xl[i]
            i += 1
            k += 1

        while j < len(xr):
            x[k] = xr[j]
            j += 1
            k += 1

assign = 0
reads = 0

def merge_sort_debug(x):
    global assign, reads
    if len(x) > 1:
        m = len(x) // 2
        xl = x[:m]
        xr = x[m:]

        reads += len(x)
        assign += len(x)

        merge_sort(xl)
        merge_sort(xr)

        i = j = k = 0
        while i < len(xl) and j < len(xr):
            if xl[i] < xr[j]:
                x[k] = xl[i]
                i += 1
            else:
                x[k] = xr[j]
                j += 1
            k += 1
            assign += 1
            reads += 2

        while i < len(xl):
            x[k] = xl[i]
            i += 1
            k += 1
            assign += 1
            reads += 1

        while j < len(xr):
            x[k] = xr[j]
            j += 1
            k += 1    
            assign += 1
            reads += 1


x = list(range(1000))
random.shuffle(x)
merge_sort_debug(x)
# print(x)
print(reads, assign)


x = list(range(250000))
random.shuffle(x)
start_time = time.time()
merge_sort(x)
end_time = time.time()
print(end_time - start_time)
