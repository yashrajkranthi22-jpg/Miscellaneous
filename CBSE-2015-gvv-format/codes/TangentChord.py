"""Generate the Class X chord/tangent figure with R on the minor arc PQ."""
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

O = np.array([[0.0], [0.0]])
r = 1.0
P = np.array([[0.0], [-1.0]])
Q = np.array([[np.cos(np.deg2rad(30))], [np.sin(np.deg2rad(30))]])
R = np.array([[np.cos(np.deg2rad(-30))], [np.sin(np.deg2rad(-30))]])
T = np.array([[1.55], [-1.0]])
fig, ax = plt.subplots(figsize=(6.5, 5.1), layout="constrained")
circle = circ_gen(O, r)
ax.plot(circle[0], circle[1], "k-", linewidth=1.7)
for X, Y in [(P, Q), (P, R), (P, T), (O, P), (O, Q)]:
    xy = line_gen(X, Y)
    ax.plot(xy[0], xy[1], linewidth=1.6)
ax.plot([O[0,0], P[0,0], Q[0,0], R[0,0], T[0,0]],
        [O[1,0], P[1,0], Q[1,0], R[1,0], T[1,0]], "ko", ms=3.5)
label_pts(np.block([O, P, Q, R, T]), ["O", "P", "Q", "R", "T"],
          offsets=[(-10,10),(-7,-15),(5,8),(5,-15),(8,-3)])
ax.add_patch(Arc((P[0,0], P[1,0]), 0.54, 0.54, theta1=0, theta2=60, linewidth=1.2))
ax.text(0.28, -0.68, r"$60^\circ$", fontsize=10)
ax.set_aspect("equal"); ax.set_xlim(-1.35, 1.85); ax.set_ylim(-1.35, 1.65)
ax.grid(True, linestyle=":", linewidth=0.5); ax.set_xlabel("x"); ax.set_ylabel("y")
for spine in ax.spines.values(): spine.set_visible(False)
out = ROOT / "figs" / "TangentChord.png"
fig.savefig(out, dpi=220, bbox_inches="tight")
plt.close(fig)
print(f"Wrote {out}")
