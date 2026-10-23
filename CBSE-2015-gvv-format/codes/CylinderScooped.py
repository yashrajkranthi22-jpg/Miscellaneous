"""Generate Q31's axial section: two radius-4.2 cm hemispherical cavities."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc
ROOT=Path(__file__).resolve().parents[1]
r=4.2; h=10.0
fig,ax=plt.subplots(figsize=(6.4,4.5),layout="constrained")
# White circles remove the material in the axial cross-section; only the
# portions inside the original cylindrical envelope represent the scoops.
ax.add_patch(Rectangle((-r,0),2*r,h,facecolor="white",edgecolor="none"))
ax.add_patch(Circle((0,0),r,facecolor="white",edgecolor="none"))
ax.add_patch(Circle((0,h),r,facecolor="white",edgecolor="none"))
# Draw surviving vertical sides and the concave semicircular edges.
ax.plot([-r,-r],[r,h-r],"k-",lw=1.6); ax.plot([r,r],[r,h-r],"k-",lw=1.6)
ax.add_patch(Arc((0,0),2*r,2*r,theta1=0,theta2=180,lw=1.6,color="black"))
ax.add_patch(Arc((0,h),2*r,2*r,theta1=180,theta2=360,lw=1.6,color="black"))
ax.annotate("",(-r-.65,0),(-r-.65,h),arrowprops=dict(arrowstyle="<->",lw=1))
ax.text(-r-1.0,h/2,"10 cm",rotation=90,ha="center",va="center",fontsize=9)
ax.annotate("",(-r,-.75),(r,-.75),arrowprops=dict(arrowstyle="<->",lw=1))
ax.text(0,-1.05,"diameter = 8.4 cm",ha="center",va="top",fontsize=9)
ax.text(0,5,"remaining metal",ha="center",fontsize=9)
ax.set_xlim(-6.3,6.0); ax.set_ylim(-1.5,11.5); ax.set_aspect("equal"); ax.axis("off")
out=ROOT/"figs"/"CylinderScooped.png"; fig.savefig(out,dpi=220,bbox_inches="tight"); fig.savefig(out.with_suffix(".eps"),format="eps",bbox_inches="tight"); plt.close(fig)
print(f"Wrote {out}")
