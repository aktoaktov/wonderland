import matplotlib.pyplot as plt

from visualization.core.grids.hexagonal import hex_grid

points = list(hex_grid((0, 5), (0, 5), 2.0))
x, y = zip(*points)

plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=50)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()