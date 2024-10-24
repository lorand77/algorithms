import time
import sys
import matplotlib.pyplot as plt

import gc

# Disable garbage collection
gc.disable()

# Initialize an empty list and variables to store timings and memory sizes
test_list = []
append_times = []
memory_sizes = []
num_elements = 100  # Number of elements to add to the list

# Measure the time taken to append each element and track memory size
for i in range(num_elements):
    start_time = time.perf_counter()
    test_list.append(i)
    end_time = time.perf_counter()
    
    # Calculate the time taken for this append operation
    append_duration = end_time - start_time
    append_times.append(append_duration)
    
    # Track the memory size of the list
    memory_size = sys.getsizeof(test_list)
    memory_sizes.append(memory_size)

# Plotting the time taken for each append
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(append_times, marker=',', linestyle='-', alpha=0.7)
plt.title("Time Taken for Each List Append Operation")
plt.xlabel("Append Operation Index")
plt.ylabel("Time (seconds)")
plt.yscale("log")  # Use logarithmic scale to highlight spikes
plt.grid(True)

# Plotting the memory size of the list over time
plt.subplot(2, 1, 2)
plt.plot(memory_sizes, marker=',', linestyle='-', alpha=0.7, color='orange')
plt.title("Memory Size of List Over Time")
plt.xlabel("Append Operation Index")
plt.ylabel("Memory Size (bytes)")
plt.grid(True)

plt.tight_layout()
plt.show()
