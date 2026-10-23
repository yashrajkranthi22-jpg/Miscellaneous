"""Generate Q19 profile; largest hemisphere base diameter equals cube side."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
ROOT=Path(__file__).resolve().parents[1]
fig,ax=plt.subplots(figsize=(5.5,4.7),layout="constrained")
# A 2-D section is sufficient to communicate the maximum inscribed base circle.
ax.add_patch(Rectangle((0,0),10,10,fill=False,lw=1.6,color="black"))
ax.add_patch(Arc((5,10),10,10,theta1=0,theta2=180,lw=1.7,color="black"))
ax.plot([0,10],[10,10],"k--",lw=.9)
ax.annotate("",(0,-.75),(10,-.75),arrowprops=dict(arrowstyle="<->",lw=1))
ax.text(5,-1.05,"10 cm",ha="center",va="top")
ax.text(5,14.1,"hemisphere: diameter 10 cm",ha="center",fontsize=9)
ax.set_xlim(-1,11); ax.set_ylim(-1.5,15); ax.set_aspect("equal"); ax.axis("off")
out=ROOT/"figs"/"CubeHemisphere.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
