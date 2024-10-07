# def find(x, v):
#     for i in range(len(x)):
#         if x[i] == v:
#             return i
#     return None


# x = [43, 8, 29, 3, 8]

# print(find(x, 3))
# print(find(x, 8))
# print(find(x, 100))
# print(find([], 54))


import time
import random

def is_even_and_gt_5(x):
    return x % 2 == 0 and x > 5

def is_odd_and_gt_7(x):
    return x % 2 == 1 and x > 7

def is_equal_to_value(x):
    return x == N_div_2

def find(x, f):
    for i in range(len(x)):
        if f(x[i]):
            return i
    return None


N = 100_000_000
N_div_2 = N // 2
x = list(range(N))
# random.shuffle(x)

start_time = time.time()
ix = find(x, is_equal_to_value)
end_time = time.time()
print(ix, end_time - start_time)

start_time = time.time()
ix = x.index(N // 2)
end_time = time.time()
print(ix, end_time - start_time)
