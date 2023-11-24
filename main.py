import random

import matplotlib.pyplot as plt

from spread_points import points_coord

fraction = 0.5
x, y = points_coord(N=300, box_x=10, box_y=10)
ind = random.choices(list(range(len(x))), k=int(len(x) * fraction))
for i in range(len(x)):
    if i in ind:
        plt.plot(x[i], y[i], "o", color="red")
    else:
        plt.plot(x[i], y[i], "o", color="black")

plt.show()
