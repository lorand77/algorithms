import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Insertion Sort Algorithm with recording of steps and color updates
def insertion_sort(data):
    steps = []  # List to store each step of the sorting process
    colors = []  # List to store the colors for each step
    n = len(data)
    
    for i in range(1, n):
        current = data[i]
        j = i - 1

        # Highlight the current element being inserted
        step_colors = ['skyblue'] * n
        step_colors[i] = 'yellow'
        steps.append(list(data))
        colors.append(list(step_colors))

        # Move elements of the sorted portion to the right to make space for current
        while j >= 0 and current < data[j]:
            data[j + 1] = data[j]
            step_colors[j + 1] = 'red'  # Mark the shifting element as red
            steps.append(list(data))
            colors.append(list(step_colors))
            
            j -= 1

        # Insert the current element
        data[j + 1] = current

        # Mark the insertion position as green
        step_colors = ['skyblue'] * n
        step_colors[j + 1] = 'green'
        steps.append(list(data))
        colors.append(list(step_colors))
    
    return steps, colors

# Function to update the bars for the animation
def update_graph(frame):
    plt.cla()  # Clear the current axes
    plt.bar(range(len(steps[frame])), steps[frame], color=colors[frame])
    plt.title(f'Insertion Sort - Step {frame + 1}/{len(steps)}')
    plt.ylim(0, max(steps[0]) + 1)

# Generate distinct random data
n = 20
data = np.random.permutation(np.arange(1, n + 1))

# Get the sorting steps and corresponding colors
steps, colors = insertion_sort(data.copy())

# Create the plot
fig, ax = plt.subplots()
ax.set_ylim(0, max(data) + 1)

# Create the animation
anim = FuncAnimation(fig, update_graph, frames=len(steps), interval=300, repeat=False)

# Show the animation
plt.show()
