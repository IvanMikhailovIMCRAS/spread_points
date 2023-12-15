from lipid import Lipid
from spread_points import points_coord
import numpy as np

z0 = 0.0
box_x, box_y = 15.0, 15.0
N = 64
x_head, y_head = points_coord(N, box_x, box_y)
L = Lipid()
x, y, z = [], [], []
types = []

for i in range(len(x_head)):
    L.create(x_head[i], y_head[i], z0, -2.0)
    x += list(L.coords[:,0])
    y += list(L.coords[:,1])
    z += list(L.coords[:,2])
    types += L.types
    if i == 0:
        bonds = L.bonds + 1 + i*11
    else:
        bonds = np.vstack([bonds, L.bonds + 1 + i*11])

with open('lipids.ent', 'w') as f:
    n = 0
    for xt, yt, zt, t in zip(x, y, z, types):
        n += 1
        f.writelines(f'HETATM{n:5d}  {t}{n:12d}{xt:12.3f}{yt:8.3f}{zt:8.3f}\n')
    for bond in bonds:
        f.writelines(f'CONECT{bond[0]:5d}{bond[1]:5d}\n')