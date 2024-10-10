import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Selection Sort Algorithm with recording of steps and color updates
def selection_sort(data):
    steps = []  # To store each step of the sorting process
    colors = []  # To store the colors for each step
    n = len(data)
    
    for i in range(n - 1, 0, -1):
        maximum = data[0]
        j_maximum = 0
        step_colors = ['skyblue'] * n  # Initialize all colors as skyblue

        # Finding the maximum element in the unsorted part
        for j in range(1, i + 1):
            step_colors[j_maximum] = 'yellow'  # Highlight current max element being compared
            step_colors[j] = 'yellow'  # Highlight the element being compared

            steps.append(list(data))
            colors.append(list(step_colors))  # Append colors before the comparison
            
            if data[j] > maximum:
                maximum = data[j]
                j_maximum = j

            step_colors[j_maximum] = 'red'  # Mark the new max after comparison
            step_colors[j] = 'skyblue'  # Reset compared element to default color

            steps.append(list(data))
            colors.append(list(step_colors))  # Append colors after the comparison

        # Swap the found maximum element with the last unsorted element
        data[j_maximum], data[i] = data[i], data[j_maximum]

        step_colors = ['skyblue'] * n
        step_colors[j_maximum] = 'green'  # Highlight swapped elements in green
        step_colors[i] = 'green'
        steps.append(list(data))
        colors.append(list(step_colors))
    
    return steps, colors

# Function to update the bars for the animation
def update_graph(frame):
    plt.cla()  # Clear the current axes
    plt.bar(range(len(steps[frame])), steps[frame], color=colors[frame])
    plt.title(f'Selection Sort - Step {frame + 1}/{len(steps)}')
    plt.ylim(0, max(steps[0]) + 1)

# Generate distinct random data
n = 20
data = np.random.permutation(np.arange(1, n + 1))

# Get the sorting steps and corresponding colors
steps, colors = selection_sort(data.copy())

# Create the plot
fig, ax = plt.subplots()
ax.set_ylim(0, max(data) + 1)

# Create the animation
anim = FuncAnimation(fig, update_graph, frames=len(steps), interval=300, repeat=False)

# Show the animation
plt.show()
