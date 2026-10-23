# CoordGeo line helpers; interfaces follow gadepall/ee1010-2026.
import numpy as np
import numpy.linalg as LA
from CoordGeo.params import omat, e1, e2

def dir_vec(A, B):
    return np.asarray(B) - np.asarray(A)

def norm_vec(A, B):
    return omat @ dir_vec(A, B)

def ang_vec(m1, m2):
    return np.arccos(float((m1.T @ m2) / (LA.norm(m1) * LA.norm(m2))))

def line_gen(A, B):
    A = np.asarray(A, dtype=float).reshape(-1, 1)
    B = np.asarray(B, dtype=float).reshape(-1, 1)
    t = np.linspace(0.0, 1.0, 100)
    return A + (B - A) @ t.reshape(1, -1)

def line_gen_num(A, B, num):
    A = np.asarray(A, dtype=float).reshape(-1, 1)
    B = np.asarray(B, dtype=float).reshape(-1, 1)
    t = np.linspace(0.0, 1.0, num)
    return A + (B - A) @ t.reshape(1, -1)

def line_dir_pt(m, A, k1, k2, num=100):
    A = np.asarray(A, dtype=float).reshape(-1, 1)
    m = np.asarray(m, dtype=float).reshape(-1, 1)
    t = np.linspace(k1, k2, num)
    return A + m @ t.reshape(1, -1)

def line_isect(n1, c1, n2, c2):
    N = np.block([n1, n2]).T
    p = np.asarray([[float(c1)], [float(c2)]])
    return LA.solve(N, p)

def line_intersect(n1, A1, n2, A2):
    N = np.block([n1, n2]).T
    p = np.asarray([[float(n1.T @ A1)], [float(n2.T @ A2)]])
    return LA.solve(N, p)

def perp_foot(n, c, P):
    m = omat @ n
    N = np.block([m, n])
    p = np.asarray([[float(m.T @ P)], [float(c)]])
    return LA.solve(N.T, p)

def rotmat(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
