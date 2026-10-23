"""Small labelling helper shared by the geometry plotting scripts."""
import numpy as np

def label_pts(points, labels, offsets=None, ax=None):
    """Label 2D column vectors; offsets are point offsets in screen points."""
    import matplotlib.pyplot as plt
    ax = ax or plt.gca()
    p = np.asarray(points, dtype=float)
    if p.ndim == 1:
        p = p.reshape(2, 1)
    if p.shape[0] != 2:
        p = p.T
    if offsets is None:
        offsets = [(5, 5)] * len(labels)
    for i, label in enumerate(labels):
        ax.annotate(label, (p[0, i], p[1, i]), xytext=offsets[i],
                    textcoords="offset points", fontsize=10)
