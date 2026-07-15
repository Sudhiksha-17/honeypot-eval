from trajectories import TRAJECTORIES, DECOY_NAIVE, DECOY_REALISTIC, N_MAL, N_BEN
from honeypot import honeypot_detect
from monitor import llm_monitor
from plot_results import plot_results

detectors = {
    "Honeypot (naive)":     lambda t: honeypot_detect(t, DECOY_NAIVE),
    "Honeypot (realistic)": lambda t: honeypot_detect(t, DECOY_REALISTIC),
    "Monitor (neutral)":    lambda t: llm_monitor(t, "neutral"),
    "Monitor (risk-aware)": lambda t: llm_monitor(t, "risk_aware"),
}

results, matrix = {}, {}
for name, fn in detectors.items():
    tp = fp = 0
    matrix[name] = {}
    for t in TRAJECTORIES:
        flagged = fn(t)
        mal = t["label"] == "malicious"
        if mal and flagged:
            tp += 1
        if (not mal) and flagged:
            fp += 1
        matrix[name][t["id"]] = (flagged == mal)
    results[name] = {"detection": tp / N_MAL, "fpr": fp / N_BEN}

print(f'\n{"Detector":24}{"Detection":12}{"FPR"}')
print("-" * 44)
for n, r in results.items():
    print(f'{n:24}{r["detection"]:.2f}        {r["fpr"]:.2f}')
print()

plot_results(results, matrix)