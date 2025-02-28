import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate points on a 4D hypersphere
def generate_hypersphere_points(num_points=1000):
    points = np.random.normal(size=(num_points, 4))  # Random points in 4D
    points /= np.linalg.norm(points, axis=1)[:, np.newaxis]  # Normalize to unit hypersphere
    return points

# Slice the hypersphere along the 4th dimension (w-axis)
def slice_hypersphere(points, w_value):
    return points[np.abs(points[:, 3] - w_value) < 0.05, :3]  # Keep only x, y, z

# Plot a 3D slice of the hypersphere
def plot_slice(slice_points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(slice_points[:, 0], slice_points[:, 1], slice_points[:, 2], s=1)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    plt.show()

# Generate and slice the hypersphere
points = generate_hypersphere_points()
for w in np.linspace(-1, 1, 10):  # Slice along the w-axis
    slice_points = slice_hypersphere(points, w)
    plot_slice(slice_points)