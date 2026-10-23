"""Numerical parameter definitions matching the EE1010 CoordGeo package."""
import numpy as np

omat = np.array([[0.0, 1.0], [-1.0, 0.0]])
R_o = np.array([[0.0, -1.0], [1.0, 0.0]])
ref = np.array([[0.0, 1.0], [1.0, 0.0]])
I = np.eye(2)
e1 = I[:, [0]]
e2 = I[:, [1]]
