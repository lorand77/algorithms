import time

def find(x, v):
    for i in range(len(x)):
        if x[i] == v:
            return i
    return None


def find_binary(x, v):
    low = 0
    high = len(x) - 1
    while low <= high:
        middle = (low + high) // 2
        if v == x[middle]:
            return middle
        if v < x[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return None


N = 100_000_000
x = list(range(N))

start_time = time.time()
ix = find_binary(x, 3)
end_time = time.time()
print(ix, end_time - start_time)


# start_time = time.time()
# ix = find(x, N // 2)
# end_time = time.time()
# print(ix, end_time - start_time)


# start_time = time.time()
# ix = x.index(N // 2)
# end_time = time.time()
# print(ix, end_time - start_time)
