"""Generate Q5 using coordinates where the two tangents meet at 120 degrees."""
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
R=np.array([[2/np.sqrt(3)],[0.]])
P=np.array([[.5*np.sqrt(3)],[.5]])
Q=np.array([[.5*np.sqrt(3)],[-.5]])
fig,ax=plt.subplots(figsize=(6.4,4.6),layout="constrained")
c=circ_gen(O,1); ax.plot(c[0],c[1],"k-",lw=1.7)
for X,Y in [(R,P),(R,Q),(O,P),(O,Q),(O,R)]:
 z=line_gen(X,Y); ax.plot(z[0],z[1],"k-",lw=1.5)
label_pts(np.block([O,P,Q,R]),["O","P","Q","R"],[(-12,-12),(-4,9),(-4,-15),(9,0)],ax)
ax.add_patch(Arc((R[0,0],0),.24,.24,theta1=120,theta2=240,lw=1.2)); ax.text(.63,.08,r"$120^\circ$",ha="center",fontsize=9)
ax.set_aspect("equal"); ax.set_xlim(-1.25,1.72); ax.set_ylim(-1.25,1.25); ax.axis("off")
out=ROOT/"figs"/"TwoTangents.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
