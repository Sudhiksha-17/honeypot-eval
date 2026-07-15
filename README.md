# Honeypot vs. LLM Monitor: A Minimal Catch-Rate Evaluation

Built for the Heron AI Security Fellowship (insider-honeypots project).

A small harness comparing honeypot detectors against an LLM monitor for catching
malicious insider-agent behavior, and testing how the comparison shifts with two
design choices: honeypot placement and monitor prompt framing.

## Setup
- 7 simulated agent trajectories (4 malicious, 3 benign) as action logs
- Honeypot tripwire at two placements: naive vs. realistic decoy paths
- LLM monitor (gpt-4o-mini) at two framings: neutral vs. risk-aware
- Metrics: detection rate, false-positive rate, per-trajectory outcomes

## Status
Harness built. Results pending.