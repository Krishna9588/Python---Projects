import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Generate points on a 4D hypersphere
def generate_hypersphere(num_points=1000):
    """Generate random points on a 4D hypersphere."""
    points = np.random.normal(size=(num_points, 4))  # Random points in 4D
    points /= np.linalg.norm(points, axis=1)[:, np.newaxis]  # Normalize to unit hypersphere
    return points

# Step 2: Slice the hypersphere along the 4th dimension (w-axis)
def slice_hypersphere(points, w_value):
    """Slice the hypersphere at a specific w-value."""
    return points[np.abs(points[:, 3] - w_value) < 0.1, :3]  # Keep only x, y, z

# Step 3: Plot a 3D slice of the hypersphere
def plot_slice(slice_points, w_value):
    """Plot the 3D slice of the hypersphere."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(slice_points[:, 0], slice_points[:, 1], slice_points[:, 2], s=1)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_title(f"3D Slice of 4D Hypersphere at w = {w_value:.2f}")
    plt.show()

# Step 4: Visualize multiple slices
def visualize_hypersphere():
    points = generate_hypersphere()
    for w in np.linspace(-1, 1, 5):  # Slice along the w-axis at 5 points
        slice_points = slice_hypersphere(points, w)
        plot_slice(slice_points, w)

# Run the program
visualize_hypersphere()