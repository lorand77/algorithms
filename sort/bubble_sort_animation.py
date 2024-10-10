import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Bubble Sort Algorithm with recording of steps and color updates
def bubble_sort(data):
    steps = []  # List to store each step of the sorting process
    colors = []  # List to store the colors for each step
    n = len(data)
    
    for i in range(n):
        for j in range(0, n-i-1):
            # Mark the elements being compared as "reading" (yellow)
            step_colors = ['skyblue'] * n
            step_colors[j] = 'yellow'
            step_colors[j + 1] = 'yellow'
            steps.append(list(data))
            colors.append(step_colors)

            if data[j] > data[j + 1]:
                # Swap if the element found is greater than the next element
                data[j], data[j + 1] = data[j + 1], data[j]

                # Mark the elements being swapped as "swapping" (red)
                step_colors = ['skyblue'] * n
                step_colors[j] = 'red'
                step_colors[j + 1] = 'red'
                steps.append(list(data))
                colors.append(step_colors)
    
    return steps, colors

# Function to update the bars for the animation
def update_graph(frame):
    plt.cla()  # Clear the current axes
    plt.bar(range(len(steps[frame])), steps[frame], color=colors[frame])
    plt.title(f'Bubble Sort - Step {frame + 1}/{len(steps)}')
    plt.ylim(0, max(steps[0]) + 1)

# Generate distinct random data
n = 20
data = np.random.permutation(np.arange(1, n + 1))

# Get the sorting steps and corresponding colors
steps, colors = bubble_sort(data.copy())

# Create the plot
fig, ax = plt.subplots()
ax.set_ylim(0, max(data) + 1)

# Create the animation
anim = FuncAnimation(fig, update_graph, frames=len(steps), interval=300, repeat=False)

# Show the animation
plt.show()
