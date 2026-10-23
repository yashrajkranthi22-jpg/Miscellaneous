"""Generate Q30 circular-segment geometry with the square and shaded caps."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch, Polygon
ROOT=Path(__file__).resolve().parents[1]
a=21.0; radius=(2*a*a)**0.5
fig,ax=plt.subplots(figsize=(6.0,5.0),layout="constrained")
# Square vertices are (+/-21,+/-21); O is the intersection of diagonals.
square=np.array([[-a,-a],[a,-a],[a,a],[-a,a],[-a,-a]])
ax.plot(square[:,0],square[:,1],"k-",lw=1.6)
# A circular segment is a true curved arc closed by the vertical chord.
def segment(theta0,theta1):
    angles=np.linspace(np.deg2rad(theta0),np.deg2rad(theta1),120)
    arc=np.column_stack((radius*np.cos(angles),radius*np.sin(angles)))
    verts=np.vstack((arc,arc[0]))
    codes=[MPath.MOVETO]+[MPath.LINETO]*(len(arc)-1)+[MPath.CLOSEPOLY]
    ax.add_patch(PathPatch(MPath(verts,codes),facecolor="white",edgecolor="black",lw=1.2,hatch="///"))
segment(135,225)  # left cap between S and P
segment(-45,45)   # right cap between Q and R
# Redraw square edges over the segment boundary for a crisp chord.
ax.plot(square[:,0],square[:,1],"k-",lw=1.6)
ax.plot([-a,a],[a,-a],"k-",lw=1.1); ax.plot([-a,a],[-a,a],"k-",lw=1.1)
for pt,label,off in [((-a,-a),"P",(-9,-13)),((a,-a),"Q",(5,-13)),((a,a),"R",(5,3)),((-a,a),"S",(-13,3)),((0,0),"O",(5,3))]:
    ax.annotate(label,pt,xytext=off,textcoords="offset points",fontsize=10)
ax.text(0,-a-4,"42 m",ha="center",fontsize=9)
ax.set_aspect("equal"); ax.set_xlim(-34,34); ax.set_ylim(-29,29); ax.axis("off")
out=ROOT/"figs"/"FlowerBeds.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
