import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# ================================================
# 4D Object Definitions
# ================================================

def generate_tesseract():
    """Generate vertices and edges of a 4D tesseract."""
    vertices = np.array([[x, y, z, w] for x in [-1, 1] for y in [-1, 1] for z in [-1, 1] for w in [-1, 1]])
    edges = [
        [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15],  # x-axis
        [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15],  # y-axis
        [0, 4], [1, 5], [2, 6], [3, 7], [8, 12], [9, 13], [10, 14], [11, 15],  # z-axis
        [0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]   # w-axis
    ]
    return vertices, edges

def generate_hypersphere(num_points=1000):
    """Generate random points on a 4D hypersphere."""
    points = np.random.normal(size=(num_points, 4))
    points /= np.linalg.norm(points, axis=1)[:, np.newaxis]  # Normalize to unit hypersphere
    return points

def generate_simplex():
    """Generate vertices and edges of a 4D simplex (pentachoron)."""
    vertices = np.array([
        [1, 1, 1, 1],
        [1, -1, -1, -1],
        [-1, 1, -1, -1],
        [-1, -1, 1, -1],
        [-1, -1, -1, 1]
    ])
    edges = [
        [0, 1], [0, 2], [0, 3], [0, 4],  # Edges from vertex 0
        [1, 2], [1, 3], [1, 4],          # Edges from vertex 1
        [2, 3], [2, 4],                  # Edges from vertex 2
        [3, 4]                           # Edges from vertex 3
    ]
    return vertices, edges

def generate_torus(R=2, r=1, num_points=1000):
    """Generate points on a 4D torus."""
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    phi = np.random.uniform(0, 2 * np.pi, num_points)
    x = (R + r * np.cos(theta)) * np.cos(phi)
    y = (R + r * np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)
    w = np.zeros(num_points)  # Add a 4th dimension
    return np.column_stack((x, y, z, w))

# ================================================
# Projection and Visualization
# ================================================

def project_to_3d(points, angle):
    """Project 4D points into 3D space using a rotation matrix."""
    rotation_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, np.cos(angle), -np.sin(angle)],
        [0, 0, np.sin(angle), np.cos(angle)]
    ])
    return np.dot(points, rotation_matrix.T)[:, :3]  # Keep only x, y, z

def plot_3d(ax, points, edges=None, color='b', size=1):
    """Plot 3D points and edges."""
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=color, s=size)
    if edges is not None:
        for edge in edges:
            ax.plot3D(*zip(points[edge[0]], points[edge[1]]), color=color)

# ================================================
# Animation
# ================================================

def animate_4d_object(points, edges=None, num_frames=100):
    """Animate a 4D object by rotating it in 4D space."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

    def update(frame):
        ax.cla()  # Clear the previous frame
        angle = 2 * np.pi * frame / num_frames
        projected_points = project_to_3d(points, angle)
        plot_3d(ax, projected_points, edges, color='b', size=10)
        ax.set_title(f"4D Object Rotation (Frame {frame + 1}/{num_frames})")

    anim = FuncAnimation(fig, update, frames=num_frames, interval=50)
    plt.show()

# ================================================
# Main Program
# ================================================

if __name__ == "__main__":
    print("Choose a 4D object to visualize:")
    print("1. Tesseract (Hypercube)")
    print("2. Hypersphere (Glome)")
    print("3. Simplex (Pentachoron)")
    print("4. Torus")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        vertices, edges = generate_tesseract()
        animate_4d_object(vertices, edges)
    elif choice == 2:
        points = generate_hypersphere()
        animate_4d_object(points)
    elif choice == 3:
        vertices, edges = generate_simplex()
        animate_4d_object(vertices, edges)
    elif choice == 4:
        points = generate_torus()
        animate_4d_object(points)
    else:
        print("Invalid choice!")