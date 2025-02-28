import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Define the 4D vertices of a tesseract (hypercube)
vertices = np.array([[x, y, z, w] for x in [-1, 1] for y in [-1, 1] for z in [-1, 1] for w in [-1, 1]])

# Define the edges of the tesseract (connections between vertices)
edges = [
    # Edges along the x-axis
    [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15],
    # Edges along the y-axis
    [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15],
    # Edges along the z-axis
    [0, 4], [1, 5], [2, 6], [3, 7], [8, 12], [9, 13], [10, 14], [11, 15],
    # Edges along the w-axis
    [0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]
]


# Function to project 4D vertices into 3D space
def project_to_3d(vertices, angle):
    # Rotation matrix for the 4th dimension (w-axis)
    rotation_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, np.cos(angle), -np.sin(angle)],
        [0, 0, np.sin(angle), np.cos(angle)]
    ])
    # Apply rotation and drop the 4th dimension
    rotated_vertices = np.dot(vertices, rotation_matrix.T)
    return rotated_vertices[:, :3]  # Keep only x, y, z


# Function to plot the tesseract in 3D
def plot_tesseract(vertices_3d, edges):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the edges
    for edge in edges:
        ax.plot3D(*zip(vertices_3d[edge[0]], vertices_3d[edge[1]]), color='b')

    # Set plot limits
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

    # Labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


# Animate the tesseract by rotating it in 4D
def animate_tesseract():
    angles = np.linspace(0, 2 * np.pi, 100)  # Rotation angles
    for angle in angles:
        vertices_3d = project_to_3d(vertices, angle)
        plot_tesseract(vertices_3d, edges)
        plt.pause(0.05)
        plt.clf()  # Clear the plot for the next frame


# Run the animation
animate_tesseract()