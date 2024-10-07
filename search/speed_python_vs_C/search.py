import time

def find(x, v):
    for i in range(len(x)):
        if x[i] == v:
            return i
    return None

N = 100_000_000
x = list(range(N))

start_time = time.time()
ix = find(x, N // 2)
end_time = time.time()
print(ix, end_time - start_time)

start_time = time.time()
ix = x.index(N // 2)
end_time = time.time()
print(ix, end_time - start_time)
