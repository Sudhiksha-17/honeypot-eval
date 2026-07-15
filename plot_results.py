import matplotlib.pyplot as plt
import numpy as np
from trajectories import TRAJECTORIES

def plot_results(results, matrix):
    names = list(results.keys())
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(14, 5))

    # Panel A
    det = [results[n]["detection"] for n in names]
    fpr = [results[n]["fpr"] for n in names]
    x = np.arange(len(names)); w = 0.35
    axA.bar(x - w / 2, det, w, label="Detection rate", color="#2E86DE")
    axA.bar(x + w / 2, fpr, w, label="False-positive rate", color="#E74C3C")
    axA.set_xticks(x); axA.set_xticklabels(names, rotation=20, ha="right")
    axA.set_ylim(0, 1); axA.set_ylabel("Rate")
    axA.set_title("Detection vs. False Positives by Detector")
    axA.legend()

    # Panel B
    ids = [t["id"] for t in TRAJECTORIES]
    grid = np.array([[1 if matrix[n][i] else 0 for n in names] for i in ids])
    axB.imshow(grid, cmap=plt.cm.RdYlGn, vmin=0, vmax=1, aspect="auto")
    axB.set_xticks(range(len(names))); axB.set_xticklabels(names, rotation=20, ha="right")
    axB.set_yticks(range(len(ids))); axB.set_yticklabels(ids)
    for i in range(len(ids)):
        for j in range(len(names)):
            axB.text(j, i, "✓" if grid[i, j] else "✗", ha="center", va="center")
    axB.set_title("Per-trajectory outcome (green=correct, red=wrong)")

    plt.tight_layout()
    plt.savefig("results.png", dpi=130)
    plt.show()