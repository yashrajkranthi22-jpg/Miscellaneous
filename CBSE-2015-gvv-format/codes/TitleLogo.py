"""Generate the title-page logo so even this image is reproducible from code."""
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figs" / "logo.jpg"
OUT.parent.mkdir(parents=True, exist_ok=True)
fig, ax = plt.subplots(figsize=(2.0, 2.0), dpi=180)
ax.set_aspect("equal")
ax.axis("off")
ax.add_patch(plt.Circle((0.5, 0.5), 0.46, fill=False, linewidth=2.2))
ax.text(0.5, 0.60, "CBSE", ha="center", va="center", fontsize=17, weight="bold")
ax.text(0.5, 0.39, "2015", ha="center", va="center", fontsize=15)
fig.savefig(OUT, bbox_inches="tight", facecolor="white", pad_inches=0.02)
# The DVI driver needs EPS; PDF/PNG builds still use the original JPEG.
fig.savefig(OUT.with_suffix(".eps"), format="eps", bbox_inches="tight", pad_inches=0.02)
plt.close(fig)
print(f"Wrote {OUT}")
