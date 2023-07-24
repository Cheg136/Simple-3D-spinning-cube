import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation

def plot_cube(angle):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
  
    vertices = np.array([[0, 0, 0],
                         [1, 0, 0],
                         [1, 1, 0],
                         [0, 1, 0],
                         [0, 0, 1],
                         [1, 0, 1],
                         [1, 1, 1],
                         [0, 1, 1]])

    edges = [[vertices[0], vertices[1], vertices[2], vertices[3], vertices[0]],
             [vertices[4], vertices[5], vertices[6], vertices[7], vertices[4]],
             [vertices[0], vertices[4]],
             [vertices[1], vertices[5]],
             [vertices[2], vertices[6]],
             [vertices[3], vertices[7]]]

    rotation_matrix = np.array([[np.cos(angle), 0, np.sin(angle)],
                                [0, 1, 0],
                                [-np.sin(angle), 0, np.cos(angle)]])
    vertices = np.dot(vertices, rotation_matrix)

    ax.add_collection3d(Poly3DCollection(edges, facecolors='none', edgecolors='b', linewidths=1))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Rotating Wireframe Cube')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

angle = 0.0
def update_animation(frame):
    global angle
    angle += np.pi / 180  # Rotate 1 degree per frame
    ax.clear()
    plot_cube(angle)

if __name__ == "__main__":
    ani = FuncAnimation(plt.gcf(), update_animation, frames=360, interval=50)
    plt.show()
