import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')


x = np.linspace(0, 2 * np.pi, 400)
ax.plot(x, np.sin(x), '--', color='gray', alpha=0.5)


circle = plt.Circle((0, 0), 0.15, color='blue')
ax.add_patch(circle)


def update(frame):
    x_pos = frame * 0.05
    y_pos = np.sin(x_pos)
    circle.center = (x_pos, y_pos)
    return circle,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=200,
    interval=30,
    blit=True
)

plt.show()
