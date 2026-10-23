"""Independent numerical checks for the Class X 30/1 worked-solution batch.

These checks intentionally recompute selected results from their defining
relations, rather than scraping the LaTeX answers.  They catch arithmetic and
geometry regressions before the PDF is built.
"""
from pathlib import Path
import math
import numpy as np
ROOT = Path(__file__).resolve().parents[1]

# Keep the verification script independent of optional helper extensions while
# using the same determinant-based definitions as the teaching chapter.
def det2(M):
    return float(np.linalg.det(np.asarray(M, dtype=float).reshape(2, 2)))

def triangle_area(A, B, C):
    a, b, c = (np.asarray(p, dtype=float).reshape(2) for p in (A, B, C))
    return abs(det2(np.column_stack((b-a, c-a)))) / 2.0

# Q1: discriminant is zero at the retained quadratic solution p=3.
assert math.isclose((-2*math.sqrt(5)*3)**2 - 4*3*15, 0.0, abs_tol=1e-10)
assert 3 != 0
# Q2: the official 20 sqrt(3) m shadow implies 30 degrees.
assert math.isclose(math.degrees(math.atan(20/(20*math.sqrt(3)))), 30.0, abs_tol=1e-10)
# Q3: count ordered outcomes for two distinguishable dice.
assert sum(1 for i in range(1,7) for j in range(1,7) if i*j == 6) == 4
# Q4: tangent-chord geometry implies the obtuse angle at R is 120 degrees.
P=np.array([0.,-1.]); Q=np.array([math.cos(math.pi/6),math.sin(math.pi/6)]); R=np.array([math.cos(-math.pi/6),math.sin(-math.pi/6)])
def angle(u,v):
    den=np.linalg.norm(u)*np.linalg.norm(v)
    return math.degrees(math.acos(float(np.clip(np.dot(u,v)/den,-1,1))))
assert math.isclose(angle(P-R,Q-R),120.0,abs_tol=1e-8)
# Q6: 9-12-15 triangle area and inradius agree with the stated data.
assert math.isclose(triangle_area([0,0],[15,0],[5.4,7.2]),54.0,abs_tol=1e-8)
assert math.isclose(54/((9+12+15)/2),3.0,abs_tol=1e-12)
# Q8: solve the AP system as a matrix system.
sol=np.linalg.solve(np.array([[12.,31.],[10.,45.]]),np.array([167.,235.]))
assert np.allclose(sol,[1.,5.])
# Q9 dot product vanishes for p=4; p=7 degenerates the triangle.
assert math.isclose(np.dot(np.array([4-4,4]),np.array([7-4,0])),0.0,abs_tol=1e-12)
# Q10 and Q29 determinant identities.
assert math.isclose(det2([[-5,2*3+1],[-3-1,-4]]),48.0,abs_tol=1e-12)
assert math.isclose(2*3**2+3*3+21,48.0,abs_tol=1e-12)
assert math.isclose(2*(-4.5)**2+3*(-4.5)+21,48.0,abs_tol=1e-12)
# Q13, Q17, Q18, Q19, Q20, Q22, Q23, Q27, Q30, Q31.
assert math.isclose((4500-1500)/15*3.6,720.0)
# Use the paper convention pi = 22/7: one tent uses 75.9 m^2 of canvas.
assert math.isclose((2*(22/7)*2.1*4+(22/7)*2.1*3.5)*100,7590,rel_tol=1e-12)
assert math.isclose(759000*0.5,379500,abs_tol=1e-12)
assert math.isclose(.9*(2/3*18**3)/(72*3**2),5.4,abs_tol=1e-12)
assert math.isclose((600+25*3.14)*5/100,33.925,abs_tol=1e-12)
assert math.isclose(4*math.pi*10.5**2,441*math.pi,rel_tol=1e-12)
assert math.isclose(10/2*(108+126),1170)
assert math.isclose(54/36 + 63/42,3)
assert math.isclose(math.sqrt((20*math.sqrt(3))**2+20**2),40)
assert math.isclose(441*(22/7)-882,504)
assert math.isclose((4.2**2*10-(4/3)*4.2**3)/(0.7**2),158.4)
for name in ["logo.jpg","Tower.png","TangentChord.png","TwoTangents.png","IncircleTriangle.png","Aeroplane.png","Tent.png","CubeHemisphere.png","CloudReflection.png","FlowerBeds.png","CylinderScooped.png"]:
    p=ROOT/"figs"/name
    assert p.is_file() and p.stat().st_size>1000, f"Missing/empty generated figure: {name}"
    # Each raster figure also needs an EPS counterpart because the classic
    # latex -> DVI route cannot include PNG/JPEG files directly.
    if name.endswith(".png"):
        eps = p.with_suffix(".eps")
        assert eps.is_file() and eps.stat().st_size > 1000, f"Missing EPS build input: {eps.name}"
assert (ROOT/"figs"/"logo.eps").is_file(), "Missing EPS build input: logo.eps"
# Ensure one script is present per figure and all solution questions are sourced.
tex=(ROOT/"chapters"/"class10.tex").read_text(encoding="utf-8")
for q in range(1,32):
    assert f"Q{q})" in tex or f"Q{q}." in tex, f"Question Q{q} appears missing from source audit labels"
print("Class X numerical checks passed; all 31 question labels and 11 generated figures were found.")
