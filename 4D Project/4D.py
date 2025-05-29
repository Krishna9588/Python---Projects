import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

points = np.random.randn(1000, 4)
points = points / np.linalg.norm(points, axis=1)[:, None]

for w in [-1, -0.5, 0, 0.5, 1]:
    sl = points[np.abs(points[:, 3] - w) < 0.1]
    sl3d = sl[:, :3]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(sl3d[:,0], sl3d[:,1], sl3d[:,2], s=1)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_title("Slice at w=%.2f" % w)
    plt.show()
