# CoordGeo matrix helpers; interfaces follow gadepall/ee1010-2026.
import numpy as np
import numpy.linalg as LA

def polyvalm(f, A):
    result = np.zeros_like(A, dtype=float)
    for i, coeff in enumerate(f):
        result += coeff * LA.matrix_power(A, len(f)-1-i)
    return result
