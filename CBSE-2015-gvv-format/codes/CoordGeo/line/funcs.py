"""Line segment sampling helpers in the column-vector style of matgeo."""
import numpy as np

def line_gen(P, Q, n=100):
    """Return a 2xN array sampling the segment P--Q."""
    p = np.asarray(P, dtype=float).reshape(2, 1)
    q = np.asarray(Q, dtype=float).reshape(2, 1)
    t = np.linspace(0.0, 1.0, n)
    return p @ (1.0 - t.reshape(1, -1)) + q @ t.reshape(1, -1)
