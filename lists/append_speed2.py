import time

N = 1_000_000

start_time = time.perf_counter()
x = []
for i in range(N):
    x.append(i)
end_time = time.perf_counter()
print(end_time - start_time)
# 120 ms

x = [0]*N
start_time = time.perf_counter()
for i in range(N):
    x[i] = i
end_time = time.perf_counter()
print(end_time - start_time)
# 120 ms

start_time = time.perf_counter()
x = list(range(N))
end_time = time.perf_counter()
print(end_time - start_time)
# 60 ms