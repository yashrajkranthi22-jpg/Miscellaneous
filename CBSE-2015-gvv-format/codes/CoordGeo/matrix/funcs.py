"""Numerically stable low-dimensional matrix operations for checks."""
import numpy as np

def dot(u, v):
    return float(np.dot(np.asarray(u, dtype=float).reshape(-1),
                        np.asarray(v, dtype=float).reshape(-1)))

def det2(M):
    M = np.asarray(M, dtype=float).reshape(2, 2)
    return float(np.linalg.det(M))

def triangle_area(A, B, C):
    """Triangle area from half the magnitude of a 2x2 determinant."""
    a, b, c = (np.asarray(p, dtype=float).reshape(2) for p in (A, B, C))
    return abs(det2(np.column_stack((b-a, c-a)))) / 2.0
