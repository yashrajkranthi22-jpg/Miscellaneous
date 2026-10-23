"""Generate the Class X tower/shadow figure using the verified 2015 value."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Coordinates use metres so that the right-triangle geometry is to scale.
A = np.array([[0.0], [20.0]])
B = np.array([[0.0], [0.0]])
C = np.array([[-20*np.sqrt(3)], [0.0]])
fig, ax = plt.subplots(figsize=(8.5, 4.7), layout="constrained")
for P, Q in [(A, B), (B, C), (A, C)]:
    xy = line_gen(P, Q)
    ax.plot(xy[0], xy[1], "k-", linewidth=2)
ax.plot([A[0,0], B[0,0], C[0,0]], [A[1,0], B[1,0], C[1,0]], "ko", ms=4)
label_pts(np.block([A, B, C]), ["A", "B", "C"], offsets=[(0,8),(8,-14),(-8,-14)])
ax.text(1.5, 10.0, r"$20\,\mathrm{m}$", ha="left", va="center")
ax.text(-10*np.sqrt(3), -2.5, r"$20\sqrt{3}\,\mathrm{m}$", ha="center", va="top")
# Given/unknown angle of elevation at C.
ax.add_patch(Arc((C[0,0], C[1,0]), 8, 8, theta1=0, theta2=30, linewidth=1.5))
ax.text(C[0,0]+4.5, 1.2, r"$\theta$", fontsize=12)
ax.set_xlim(-39, 5); ax.set_ylim(-4, 24)
ax.set_aspect("equal", adjustable="box"); ax.axis("off")
out = ROOT / "figs" / "Tower.png"
fig.savefig(out, dpi=220, bbox_inches="tight")
plt.close(fig)
print(f"Wrote {out}")
