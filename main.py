import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from prim import mst_prim


A = np.loadtxt('ha30_dist.txt', dtype=int)
G = nx.from_numpy_matrix(A)

r = 1
mst = mst_prim(G, r)

nx.draw(mst, with_labels=True)
plt.draw()
plt.show()