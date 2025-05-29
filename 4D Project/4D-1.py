import numpy as np
import matplotlib.pyplot as plt


# generate some 4d points

pts = np.random.normal(0, 1, (1000, 4))
norms = np.linalg.norm(pts, axis=1)
pts = pts / norms[:, np.newaxis]


ws = [-1, -0.5, 0, 0.5, 1]



for val in ws:
    mask = np.abs(pts[:,3] - val) < 0.1
    sliced = pts[mask]
    xyz = sliced[:, :3]

    
    f = plt.figure()
    ax = f.add_subplot(111, projection='3d')
    ax.scatter(xyz[:,0], xyz[:,1], xyz[:,2], s=2)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_title("w=%.2f"%val)
    plt.show()
