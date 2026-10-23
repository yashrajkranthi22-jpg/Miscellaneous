# CoordGeo triangle helpers; interfaces follow gadepall/ee1010-2026.
import numpy as np
import numpy.linalg as LA
from CoordGeo.line.funcs import dir_vec, norm_vec, line_intersect

def tri_sides(A, B, C):
    return LA.norm(A-B), LA.norm(B-C), LA.norm(C-A)

def tri_vert(a, b, c):
    p = (a*a + c*c - b*b)/(2*a)
    q = np.sqrt(max(0.0, c*c-p*p))
    return np.array([[p],[q]]), np.array([[0.0],[0.0]]), np.array([[a],[0.0]])

def tri_mid_pt(A, B, C):
    return (B+C)/2, (C+A)/2, (A+B)/2

def ccircle(A, B, C):
    D, E, F = tri_mid_pt(A, B, C)
    m1, m2 = dir_vec(A, B), dir_vec(A, C)
    O = line_intersect(m1, F, m2, E)
    return O, LA.norm(A-O)
