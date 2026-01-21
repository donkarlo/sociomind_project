import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
import numpy as np

# Example data
x1 = np.array([0, 1, 2, 3])
y1 = np.array([1, 2, 1, 2])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([2, 1, 2, 1])

fig, ax = plt.subplots()

# Scatter points for both datasets
ax.scatter(x1, y1)
ax.scatter(x2, y2)

# Connect corresponding points
for i in range(len(x1)):
    ax.plot([x1[i], x2[i]], [y1[i], y2[i]])

plt.show()