"""Generate Q2 from the verified 20 m by 20 sqrt(3) m right triangle."""
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
A = np.array([[0.0], [20.0]])
B = np.array([[0.0], [0.0]])
C = np.array([[-20*np.sqrt(3)], [0.0]])
fig, ax = plt.subplots(figsize=(8.2, 4.2), layout="constrained")
for P,Q in [(A,B),(B,C),(A,C)]:
    z=line_gen(P,Q); ax.plot(z[0],z[1],"k-",lw=1.8)
label_pts(np.block([A,B,C]), ["A","B","C"], [(0,7),(7,-13),(-8,-13)])
ax.text(1.2,10,r"$20\,\mathrm{m}$",va="center")
ax.text(-10*np.sqrt(3),-2.1,r"$20\sqrt{3}\,\mathrm{m}$",ha="center",va="top")
ax.add_patch(Arc((C[0,0],0),8,8,theta1=0,theta2=30,lw=1.2))
ax.text(C[0,0]+4.5,1.0,r"$\theta$",fontsize=12)
ax.set_xlim(-39,5); ax.set_ylim(-4,24); ax.set_aspect("equal"); ax.axis("off")
out=ROOT/"figs"/"Tower.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
