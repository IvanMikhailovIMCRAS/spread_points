import numpy as np
from ase import Atoms
import ase.visualize
import IPython

def random_vector(length=1):
    vector = 1.0 -2.0*np.random.random(3)
    r = np.sqrt(np.sum(vector**2))
    return vector/r*length

class Lipid():
    def __init__(self):
        self.bonds = [
            [1,0],
            [2,1],
            [3,2],
            [4,3],
            [5,4],
            [6,5],
            [7,2],
            [8,7],
            [9,8],
            [10,9]
        ]
        self.types = ['O']*3+['N']*8
        self.coords = np.zeros(shape=(11,3), dtype = float)
    def create(self, x0, y0, z0):
        self.coords[0,0] = x0
        self.coords[0,1] = y0
        self.coords[0,2] = z0
        for bond in self.bonds:
            self.coords[bond[0]] = self.coords[bond[1]] + random_vector()
        
# if __name__== '__main__':
L = Lipid()
L.create(0, 0, 1)
    # print(L.coords)


symbols = L.types
position = L.coords

system = Atoms(positions=position, symbols=symbols)

ase.visualize.view(system, viewer="x3d")