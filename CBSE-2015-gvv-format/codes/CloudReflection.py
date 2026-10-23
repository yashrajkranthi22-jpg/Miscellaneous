"""Generate Q27 geometry; a still-water reflection is symmetric about y=0."""
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
x=20*(3**0.5); H=40
fig,ax=plt.subplots(figsize=(7.6,4.3),layout="constrained")
ax.plot([-4,x+5],[0,0],"k-",lw=1.5)
ax.text(x+4.8,-.35,"lake surface",ha="right",fontsize=9)
ax.plot([0,0],[-H-3,H+5],"k:",lw=.9)
ax.plot([0,x],[20,H],"k-",lw=1.6)
ax.plot([0,x],[20,-H],"k--",lw=1.3)
ax.plot([0,x,x],[20,H,-H],"ko",ms=3)
ax.text(-.35,20,"A (20 m)",ha="right",va="center",fontsize=9)
ax.text(x+1,H,"cloud",va="center",fontsize=9)
ax.text(x+1,-H,"reflection",va="center",fontsize=9)
ax.text(x/2,33,r"$30^\circ$",fontsize=10)
ax.text(x/2,2,r"$60^\circ$",fontsize=10)
ax.text(x/2,-2,r"$x=20\sqrt{3}$ m",ha="center",fontsize=9)
ax.set_xlim(-4,x+10); ax.set_ylim(-47,52); ax.axis("off")
out=ROOT/"figs"/"CloudReflection.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
