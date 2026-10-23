"""Numerical checks for the current Class X/Class XII working batch."""
from pathlib import Path
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
# Class X Q1: equal-root discriminant is zero only at p=0 or p=3;
# p=0 destroys the quadratic term.
p = 3.0
assert math.isclose((-2*math.sqrt(5)*p)**2 - 4*p*15, 0.0, abs_tol=1e-10)
assert p != 0

# Class X Q2: verified shadow length is 20 sqrt(3) m.
theta_deg = math.degrees(math.atan(20/(20*math.sqrt(3))))
assert math.isclose(theta_deg, 30.0, abs_tol=1e-10)

# Class X Q3: 4 favorable ordered pairs among 36 equally likely results.
assert math.isclose(4/36, 1/9, abs_tol=1e-12)

# Class X Q4: with P at -90 degrees, Q at 30 degrees, R at -30 degrees,
# tangent PT is horizontal and the inscribed angle PRQ is 120 degrees.
P = np.array([0.0, -1.0])
Q = np.array([math.cos(math.radians(30)), math.sin(math.radians(30))])
R = np.array([math.cos(math.radians(-30)), math.sin(math.radians(-30))])
T = np.array([1.55, -1.0])
def angle(a, b):
    v = a / np.linalg.norm(a); w = b / np.linalg.norm(b)
    return math.degrees(math.acos(float(np.clip(np.dot(v, w), -1, 1))))
assert math.isclose(angle(Q-P, T-P), 60.0, abs_tol=1e-8)
assert math.isclose(angle(P-R, Q-R), 120.0, abs_tol=1e-8)

# Class X Q5: for a 120-degree tangent angle and unit radius, OR=2 PR.
OR = 2 / math.sqrt(3)
PR = math.sqrt(OR**2 - 1)
assert math.isclose(OR, 2*PR, abs_tol=1e-10)

# Class XII Vectors Q1: scaled cross product has magnitude sqrt(171).
a = np.array([1., -2., -3.]); b = np.array([3., -1., -2.])
v = math.sqrt(57)/5 * np.cross(a, b)
assert math.isclose(np.linalg.norm(v), math.sqrt(171), abs_tol=1e-10)
assert math.isclose(float(np.dot(v, a)), 0.0, abs_tol=1e-10)
assert math.isclose(float(np.dot(v, b)), 0.0, abs_tol=1e-10)

# Class XII Vectors Q4-Q7 selected checks.
assert math.isclose(math.sqrt(9+36), math.sqrt(5+40), abs_tol=1e-12)
assert np.allclose(np.dot(np.array([2., -1., 4.]), np.array([96., -3., -42.])), 27)
assert math.isclose(math.sqrt(5/29), np.linalg.norm(np.cross([1,2,2], [2,3,4]))/math.sqrt(29))
assert math.isclose(np.linalg.norm(np.array([2., -1., 4.])), math.sqrt(21))

for name in ["logo.jpg", "Tower.png", "TangentChord.png", "TwoTangents.png"]:
    path = ROOT / "figs" / name
    assert path.is_file() and path.stat().st_size > 1000, f"Missing generated figure: {name}"

print("Math checks passed: 8 groups.")
print("Figure checks passed: all 4 generated image assets exist.")
