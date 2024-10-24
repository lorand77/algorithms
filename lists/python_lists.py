# For lists in Python, compare the speed of operations like v=x[i], x[i]=v, append, insert (middle), pop (middle) (also del x[i]), find (x.index) (middle value+10), reverse, sort (that is try to get results for average case, therefore for sort use randomly shuffled list). Use N=1,000,000 and use timeit with 1000 repetitions for element access and assignment, 10 repetitions for the rest. Divide with the number of repetitions and provide the results in milliseconds. Just write the code, do not run it.

import timeit

N = 1_000_000
repetitions_element_ops = 10000
repetitions_other_ops = 1000
repetitions_sort = 1

# Prepare a sample list and random middle index
x = list(range(N))
middle_index = N // 2

# Time element access
time_access = timeit.timeit(
    stmt="v = x[middle_index]",
    setup="from __main__ import x, middle_index",
    number=repetitions_element_ops
) / repetitions_element_ops * 1000

# Time element assignment
time_assignment = timeit.timeit(
    stmt="x[middle_index] = 500000",
    setup="from __main__ import x, middle_index",
    number=repetitions_element_ops
) / repetitions_element_ops * 1000

# Time append operation
time_append = timeit.timeit(
    stmt="x.append(1)",
    setup="from __main__ import x",
    number=repetitions_element_ops
) / repetitions_element_ops * 1000

# Time insert operation (middle)
time_insert = timeit.timeit(
    stmt="x.insert(middle_index, 999999)",
    setup="from __main__ import x, middle_index",
    number=repetitions_other_ops
) / repetitions_other_ops * 1000

time_insert = timeit.timeit(
    stmt="x.insert(middle_index, 999999)",
    setup="from __main__ import x, middle_index",
    number=repetitions_other_ops
) / repetitions_other_ops * 1000

# Time pop operation (middle)
time_pop = timeit.timeit(
    stmt="x.pop(middle_index)",
    setup="from __main__ import x, middle_index",
    number=repetitions_other_ops
) / repetitions_other_ops * 1000

# Time del operation (middle)
time_del = timeit.timeit(
    stmt="del x[middle_index]",
    setup="from __main__ import x, middle_index",
    number=repetitions_other_ops
) / repetitions_other_ops * 1000

# Time find (x.index) operation
value_to_find = middle_index
time_index = timeit.timeit(
    stmt="x.index(value_to_find)",
    setup="from __main__ import x, value_to_find",
    number=repetitions_other_ops
) / repetitions_other_ops * 1000

# Time reverse operation
time_reverse = timeit.timeit(
    stmt="x.reverse()",
    setup="from __main__ import x",
    number=repetitions_other_ops
) / repetitions_other_ops * 1000

# Prepare a randomly shuffled list for sort operation
import random
x_random = list(range(N))
random.shuffle(x_random)

# Time sort operation
time_sort = timeit.timeit(
    stmt="x_random.sort()",
    setup="from __main__ import x_random",
    number=repetitions_sort
) / repetitions_sort * 1000

# Display results
print(f"Element access (v=x[i]): {time_access:.6f} ms")
print(f"Element assignment (x[i]=v): {time_assignment:.6f} ms")
print(f"Append: {time_append:.6f} ms")
print(f"Insert (middle): {time_insert:.6f} ms")
print(f"Pop (middle): {time_pop:.6f} ms")
print(f"Del (middle): {time_del:.6f} ms")
print(f"Find (x.index, middle value): {time_index:.6f} ms")
print(f"Reverse: {time_reverse:.6f} ms")
print(f"Sort (randomly shuffled list): {time_sort:.6f} ms")



# Element access (v=x[i]): 0.000 023 ms
# Element assignment (x[i]=v): 0.000 023 ms

# Append: 0.018 505 ms     1000x

# Insert (middle): 0.629835 ms     20-30x
# Pop (middle): 0.385940 ms
# Del (middle): 0.402495 ms

# Reverse: 0.852356 ms        2x

# Find (x.index, middle value+10): 6.919700 ms      10x    O(n)

# Sort (randomly shuffled list): 54.195658 ms      8x     O(n*log(n))


# Element access (v=x[i]): 0.000021 ms
# Element assignment (x[i]=v): 0.000021 ms

# Append: 0.000042 ms            2x

# Insert (middle): 0.453438 ms       1000x
# Pop (middle): 0.379222 ms
# Del (middle): 0.349852 ms

# Reverse: 0.974432 ms          2-3x

# Find (x.index, middle value): 6.489376 ms     300_000x access    O(n)
# Sort (randomly shuffled list): 376.929499 ms   60x             O(n*log(n))  log(n)=20