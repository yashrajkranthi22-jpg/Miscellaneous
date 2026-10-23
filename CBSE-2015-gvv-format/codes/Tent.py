"""Generate a cross-section of the open-bottom cylinder/cone tent in Q17."""
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
r=2.1; hc=4.0; hcone=2.8
fig,ax=plt.subplots(figsize=(6.5,4.8),layout="constrained")
# Cross-section only: the open bottom is intentionally not drawn as a canvas face.
ax.plot([-r,-r],[0,hc],"k-",lw=1.7); ax.plot([r,r],[0,hc],"k-",lw=1.7)
ax.plot([-r,r],[hc,hc],color="black",lw=1.0,ls="--")
ax.plot([-r,0],[hc,hc+hcone],"k-",lw=1.7); ax.plot([r,0],[hc,hc+hcone],"k-",lw=1.7)
ax.plot([-r,r],[0,0],"k:",lw=1.0)
ax.annotate("",(-r-.38,0),(-r-.38,hc),arrowprops=dict(arrowstyle="<->",lw=1))
ax.text(-r-.55,hc/2,"4 m",rotation=90,va="center",ha="center")
ax.annotate("",(r+.38,hc),(r+.38,hc+hcone),arrowprops=dict(arrowstyle="<->",lw=1))
ax.text(r+.58,hc+hcone/2,"2.8 m",rotation=90,va="center",ha="center")
ax.text(0,hc-.35,"cylindrical part",ha="center",fontsize=9)
ax.text(0,hc+hcone/2,"conical part",ha="center",fontsize=9)
ax.text(0,-.4,"diameter = 4.2 m",ha="center",fontsize=9)
ax.set_xlim(-3.2,3.5); ax.set_ylim(-.7,7.4); ax.set_aspect("equal"); ax.axis("off")
out=ROOT/"figs"/"Tent.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
