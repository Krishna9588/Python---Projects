import numpy as np
import matplotlib.pyplot as plt

verts = np.array([[x, y, z, w] for x in [-1, 1] for y in [-1, 1] for z in [-1, 1] for w in [-1, 1]])



edges = [
    [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15],
    [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15],
    [0, 4], [1, 5], [2, 6], [3, 7], [8, 12], [9, 13], [10, 14], [11, 15],
    [0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]
]


angles = np.linspace(0, 2 * np.pi, 100)

for a in angles:
    rot = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, np.cos(a), -np.sin(a)],
        [0, 0, np.sin(a),  np.cos(a)]
    ])
    
    v3 = np.dot(verts, rot.T)[:, :3]

    plt.clf()
    ax = plt.axes(projection='3d')
    for e in edges:
        xs, ys, zs = zip(v3[e[0]], v3[e[1]])
        ax.plot(xs, ys, zs, 'b')

    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_zlim(-2,2)
    plt.pause(0.05)

plt.close()
