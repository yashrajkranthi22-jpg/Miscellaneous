"""Triangle routines expressed through coordinate determinants."""
from CoordGeo.matrix.funcs import triangle_area

def area2d(A, B, C):
    return triangle_area(A, B, C)
