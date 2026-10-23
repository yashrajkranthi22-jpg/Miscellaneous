"""Generate Q13's fixed-altitude plane positions at 60 and 30 degrees."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
ROOT=Path(__file__).resolve().parents[1]
# Normalize altitude to 3 drawing units; ranges scale by cot(theta).
h=3.0; x1=h/(3**0.5); x2=h*(3**0.5)
fig,ax=plt.subplots(figsize=(8.0,3.7),layout="constrained")
ax.plot([-0.4,6.1],[0,0],"k-",lw=1.4)
ax.plot([x1,x2],[h,h],"k-",lw=1.4)
ax.plot([x1,x1],[0,h],"k--",lw=1.0); ax.plot([x2,x2],[0,h],"k--",lw=1.0)
ax.plot([0,x1],[0,h],"k-",lw=1.5); ax.plot([0,x2],[0,h],"k-",lw=1.5)
ax.plot([0,x1,x2],[0,h,h],"ko",ms=3)
ax.text(-.15,-.25,"A",ha="right"); ax.text(x1,h+.18,"P₁",ha="center"); ax.text(x2,h+.18,"P₂",ha="center")
ax.text((x1+x2)/2,h+.5,"constant altitude",ha="center",fontsize=9)
ax.text(x1-.12,1.1,r"$60^\circ$",ha="right",fontsize=10); ax.text(1.6,.52,r"$30^\circ$",fontsize=10)
ax.text((x1+x2)/2,-.35,r"$3000\,\mathrm{m}$",ha="center",fontsize=10)
ax.set_xlim(-.5,6.3); ax.set_ylim(-.65,4.1); ax.axis("off")
out=ROOT/"figs"/"Aeroplane.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
