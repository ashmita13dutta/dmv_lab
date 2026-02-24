import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

line, = ax.plot([], [], lw=2)
x = np.linspace(0, 2*np.pi, 400)

def update(frame):
    y = np.sin(x + frame * 0.1)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
