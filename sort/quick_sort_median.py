import random
import time
import sys

sys.setrecursionlimit(1000000)

def quick_sort(x):
    if len(x) > 1:
        i_l = 0
        i_h = len(x) - 1
        i_m = (i_l + i_h) // 2
        if (x[i_l] > x[i_m] and x[i_l] < x[i_h]) or (x[i_l] < x[i_m] and x[i_l] > x[i_h]):
            i_pivot = i_l
        elif (x[i_m] > x[i_l] and x[i_m] < x[i_h]) or (x[i_m] < x[i_l] and x[i_m] > x[i_h]):
            i_pivot = i_m
        else:
            i_pivot = i_h
        
        pivot = x[i_pivot]
        xl = []
        xr = []
        for i in range(len(x)):
            if i != i_pivot:
                if x[i] <= pivot:
                    xl.append(x[i])
                else:
                    xr.append(x[i])

        return quick_sort(xl) + [pivot] + quick_sort(xr)
    else:
        return x    


assign = 0
reads = 0

def quick_sort_debug(x):
    global assign, reads
    if len(x) > 1:
        i_l = 0
        i_h = len(x) - 1
        i_m = (i_l + i_h) // 2
        if (x[i_l] > x[i_m] and x[i_l] < x[i_h]) or (x[i_l] < x[i_m] and x[i_l] > x[i_h]):
            i_pivot = i_l
        elif (x[i_m] > x[i_l] and x[i_m] < x[i_h]) or (x[i_m] < x[i_l] and x[i_m] > x[i_h]):
            i_pivot = i_m
        else:
            i_pivot = i_h
        
        pivot = x[i_pivot]

        assign += 1
        reads += 3
        xl = []
        xr = []
        for i in range(len(x)):
            if i != i_pivot:
                if x[i] <= pivot:
                    xl.append(x[i])
                else:
                    xr.append(x[i])
                assign += 1
                reads += 1
        return quick_sort_debug(xl) + [pivot] + quick_sort_debug(xr)
    else:
        return x


x = list(range(1000))
#random.shuffle(x)
quick_sort_debug(x)
# print(quick_sort_debug(x))
print(reads, assign)


x = list(range(350000))
random.shuffle(x)
start_time = time.time()
quick_sort(x)
end_time = time.time()
print(end_time - start_time)
