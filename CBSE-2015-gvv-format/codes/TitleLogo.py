"""Generate the small title-page mark used by main.tex."""
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figs" / "logo.jpg"
OUT.parent.mkdir(parents=True, exist_ok=True)
fig, ax = plt.subplots(figsize=(2.0, 2.0), dpi=180)
ax.axis("off")
ax.add_patch(plt.Circle((0.5, 0.5), 0.46, fill=False, linewidth=2.2))
ax.text(0.5, 0.59, "CBSE", ha="center", va="center", fontsize=18, weight="bold")
ax.text(0.5, 0.39, "2015", ha="center", va="center", fontsize=16)
fig.savefig(OUT, bbox_inches="tight", facecolor="white", pad_inches=0.02)
plt.close(fig)
print(f"Wrote {OUT}")
