"""Circle sampling helper."""
import numpy as np

def circ_gen(O, r, n=361):
    """Return a 2xN array of points on a circle centered at column vector O."""
    o = np.asarray(O, dtype=float).reshape(2, 1)
    theta = np.linspace(0, 2*np.pi, n)
    return o + float(r) * np.vstack((np.cos(theta), np.sin(theta)))
