import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Helper function to merge two halves for animation
def merge(x, start, mid, end, steps, colors):
    xl = x[start:mid]  # Left sublist
    xr = x[mid:end]  # Right sublist

    i = j = 0
    k = start

    # Initial colors for the merge operation
    step_colors = ['skyblue'] * len(x)

    # Make a copy of the original list to avoid in-place modification
    current_data = list(x)

    # Merge the two halves while maintaining order
    while i < len(xl) and j < len(xr):
        step_colors[start + i] = 'yellow'  # Highlight left part being compared
        step_colors[mid + j] = 'yellow'  # Highlight right part being compared
        steps.append(list(current_data))
        colors.append(list(step_colors))
        
        if xl[i] < xr[j]:
            current_data[k] = xl[i]
            step_colors[k] = 'green'  # Highlight position being filled
            i += 1
        else:
            current_data[k] = xr[j]
            step_colors[k] = 'green'  # Highlight position being filled
            j += 1
        k += 1
        
        # Reset comparison colors
        step_colors = ['skyblue'] * len(x)
        step_colors[start + i:mid] = ['skyblue'] * (mid - start - i)
        step_colors[mid + j:end] = ['skyblue'] * (end - mid - j)
    
    # Copy the remaining elements from the left sublist
    while i < len(xl):
        current_data[k] = xl[i]
        step_colors[k] = 'green'
        steps.append(list(current_data))
        colors.append(list(step_colors))
        i += 1
        k += 1

    # Copy the remaining elements from the right sublist
    while j < len(xr):
        current_data[k] = xr[j]
        step_colors[k] = 'green'
        steps.append(list(current_data))
        colors.append(list(step_colors))
        j += 1
        k += 1

    # Update the main array with the merged data
    x[start:end] = current_data[start:end]

# Recursive function to sort and track the steps
def merge_sort_animate(x, start, end, steps, colors):
    if end - start > 1:
        mid = (start + end) // 2

        # Recursively split the list into two halves
        merge_sort_animate(x, start, mid, steps, colors)
        merge_sort_animate(x, mid, end, steps, colors)

        # Merge the sorted halves
        merge(x, start, mid, end, steps, colors)

# Wrapper to setup steps and initiate the merge sort animation
def merge_sort_visual(x):
    steps = []  # To store each step of the sorting process
    colors = []  # To store the colors for each step
    merge_sort_animate(x, 0, len(x), steps, colors)
    return steps, colors

# Function to update the bars for the animation
def update_graph(frame):
    plt.cla()  # Clear the current axes
    plt.bar(range(len(steps[frame])), steps[frame], color=colors[frame])
    plt.title(f'Merge Sort - Step {frame + 1}/{len(steps)}')
    plt.ylim(0, max(steps[0]) + 1)

# Generate distinct random data
n = 20
data = np.random.permutation(np.arange(1, n + 1))

# Get the sorting steps and corresponding colors
steps, colors = merge_sort_visual(data.copy())

# Create the plot
fig, ax = plt.subplots()
ax.set_ylim(0, max(data) + 1)

# Create the animation
anim = FuncAnimation(fig, update_graph, frames=len(steps), interval=300, repeat=False)

# Show the animation
plt.show()
