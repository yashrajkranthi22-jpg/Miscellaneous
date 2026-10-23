# CoordGeo conic helpers; interfaces follow gadepall/ee1010-2026.
import numpy as np
import numpy.linalg as LA
from CoordGeo.params import ref

def circ_gen(O, r):
    theta = np.linspace(0, 2*np.pi, 361)
    O = np.asarray(O, dtype=float).reshape(2, 1)
    return O + r*np.vstack((np.cos(theta), np.sin(theta)))

def circ_gen_num(O, r, num):
    theta = np.linspace(0, 2*np.pi, num)
    O = np.asarray(O, dtype=float).reshape(2, 1)
    return O + r*np.vstack((np.cos(theta), np.sin(theta)))

def ellipse_gen(a, b):
    theta = np.linspace(0, 2*np.pi, 361)
    return np.vstack((a*np.cos(theta), b*np.sin(theta)))

def ellipse_gen_num(a, b, num):
    theta = np.linspace(0, 2*np.pi, num)
    return np.vstack((a*np.cos(theta), b*np.sin(theta)))

def parab_gen(y, a):
    return y**2 / a

def hyper_gen(y):
    return np.sqrt(1 + y**2)

def circ_param(u, f):
    u = np.asarray(u, dtype=float)
    O = -u
    r = np.sqrt(LA.norm(u)**2 - f)
    return O, r

def ellipse_param(V, u, f):
    lam, _ = LA.eig(V)
    f0 = u.T @ LA.inv(V) @ u - f
    return np.sqrt(np.abs(f0 / lam)).flatten()
