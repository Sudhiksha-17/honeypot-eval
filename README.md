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

## Run

    pip install openai python-dotenv matplotlib numpy
    # add OPENAI_API_KEY to .env
    python run_eval.py

## Results (initial run)

    Detector                Detection   FPR
    Honeypot (naive)        0.25        0.00
    Honeypot (realistic)    0.25        0.33
    Monitor (neutral)       0.50        0.00
    Monitor (risk-aware)    1.00        0.00

![results](results_initial.png)

## What I'm seeing
- Honeypots only fire on decoy contact -> careful attacker (real target) and sabotage
  (no file touched) both slip past.
- Placement matters -> naive decoy = no false alarms, realistic decoy = false-positives
  a benign agent that legit reads it.
- Framing matters: same monitor, neutral gets half, risk-aware gets all. Just the prompt.

## Provisional conclusion
Take this alone, this looks like the risk-aware monitor dominates. But the comparison
already depends heavily on placement and framing, so the numbers should not be read
as a straightforward ranking.

