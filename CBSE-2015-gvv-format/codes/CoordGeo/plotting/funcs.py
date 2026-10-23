# CoordGeo plotting helpers; label_pts matches the course repository API.
import numpy as np
import matplotlib.pyplot as plt

def label_pts(G_v, vert_labels, offsets=None):
    G_v = np.asarray(G_v, dtype=float)
    if G_v.ndim == 1:
        G_v = G_v.reshape(2, 1)
    if offsets is None:
        offsets = [(0, 10)] * G_v.shape[1]
    for i, txt in enumerate(vert_labels):
        plt.annotate(txt, (G_v[0, i], G_v[1, i]), textcoords="offset points",
                     xytext=offsets[i], ha="center")
