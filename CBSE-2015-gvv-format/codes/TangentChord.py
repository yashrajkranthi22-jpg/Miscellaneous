"""Generate Q4; points are placed on a unit circle with R on minor arc PQ."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent
sys.path.insert(0,str(HERE))
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts
O=np.array([[0.],[0.]])
P=np.array([[0.],[-1.]])
Q=np.array([[np.cos(np.deg2rad(30))],[np.sin(np.deg2rad(30))]])
R=np.array([[np.cos(np.deg2rad(-30))],[np.sin(np.deg2rad(-30))]])
T=np.array([[1.55],[-1.]])
fig,ax=plt.subplots(figsize=(6.2,5.0),layout="constrained")
c=circ_gen(O,1); ax.plot(c[0],c[1],"k-",lw=1.6)
for X,Y,style in [(P,Q,"k-"),(P,R,"k-"),(P,T,"k-"),(O,P,"k--"),(O,Q,"k--")]:
 z=line_gen(X,Y); ax.plot(z[0],z[1],style,lw=1.5)
label_pts(np.block([O,P,Q,R,T]),["O","P","Q","R","T"],[(-12,10),(-6,-16),(5,8),(6,-14),(7,-3)],ax)
ax.add_patch(Arc((P[0,0],P[1,0]),.52,.52,theta1=0,theta2=60,lw=1.1)); ax.text(.26,-.68,r"$60^\circ$",fontsize=9)
ax.set_aspect("equal"); ax.set_xlim(-1.3,1.82); ax.set_ylim(-1.35,1.65); ax.axis("off")
out=ROOT/"figs"/"TangentChord.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
