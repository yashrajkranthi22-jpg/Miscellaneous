"""Generate the Class X two-tangents figure (angle PRQ = 120 degrees)."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

r = 1.0
O = np.array([[0.0], [0.0]])
d = 2 / np.sqrt(3)
R = np.array([[d], [0.0]])
P = np.array([[np.cos(np.deg2rad(30))], [np.sin(np.deg2rad(30))]])
Q = np.array([[np.cos(np.deg2rad(30))], [-np.sin(np.deg2rad(30))]])
fig, ax = plt.subplots(figsize=(6.3, 4.7), layout="constrained")
circ = circ_gen(O, r)
ax.plot(circ[0], circ[1], linewidth=1.7)
for X, Y in [(R, P), (R, Q), (O, P), (O, Q), (O, R)]:
    xy = line_gen(X, Y)
    ax.plot(xy[0], xy[1], linewidth=1.6)
ax.plot([O[0,0], P[0,0], Q[0,0], R[0,0]], [O[1,0], P[1,0], Q[1,0], R[1,0]], "ko", ms=3.7)
label_pts(np.block([O, P, Q, R]), ["O", "P", "Q", "R"], offsets=[(-12,-12),(-5,9),(-5,-15),(9,0)])
ax.add_patch(Arc((R[0,0], R[1,0]), 0.23, 0.23, theta1=120, theta2=240, linewidth=1.2))
ax.text(0.62, 0.12, r"$120^\circ$", ha="center", va="bottom", fontsize=10)
ax.set_aspect("equal"); ax.set_xlim(-1.25, 1.75); ax.set_ylim(-1.25, 1.25)
ax.grid(True, linestyle=":", linewidth=0.5); ax.set_xlabel("x"); ax.set_ylabel("y")
for spine in ax.spines.values(): spine.set_visible(False)
out = ROOT / "figs" / "TwoTangents.png"
fig.savefig(out, dpi=220, bbox_inches="tight")
plt.close(fig)
print(f"Wrote {out}")
