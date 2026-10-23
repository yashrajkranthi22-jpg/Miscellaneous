"""Generate Q6 from the exact 9-12-15 triangle and its incircle."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent
sys.path.insert(0,str(HERE))
from CoordGeo.line.funcs import line_gen
B=np.array([[0.],[0.]])
D=np.array([[6.],[0.]])
C=np.array([[15.],[0.]])
A=np.array([[5.4],[7.2]])
O=np.array([[6.],[3.]])
fig,ax=plt.subplots(figsize=(7.5,4.5),layout="constrained")
for X,Y in [(A,B),(A,C),(B,C)]:
 z=line_gen(X,Y); ax.plot(z[0],z[1],"k-",lw=1.6)
ax.add_patch(Circle((O[0,0],O[1,0]),3,fill=False,color="black",lw=1.4))
ax.plot([O[0,0],D[0,0]],[O[1,0],D[1,0]],"k--",lw=1)
for point,label,off in [(A,"A",(0,8)),(B,"B",(-10,-14)),(D,"D",(-2,-16)),(C,"C",(6,-14)),(O,"O",(5,2))]:
 ax.annotate(label,(point[0,0],point[1,0]),xytext=off,textcoords="offset points",fontsize=10)
ax.text(3,3.6,r"$r=3$ cm",fontsize=9); ax.text(3,-.8,"6 cm",ha="center"); ax.text(10.5,-.8,"9 cm",ha="center")
ax.set_xlim(-1,16); ax.set_ylim(-1.8,9); ax.set_aspect("equal"); ax.axis("off")
out=ROOT/"figs"/"IncircleTriangle.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
