# Honeypot vs. LLM Monitor: A Minimal Catch-Rate Evaluation

Built for the Heron AI Security Fellowship (insider-honeypots project).

A small harness comparing honeypot detectors against an LLM monitor for catching
malicious insider-agent behavior, and testing how the comparison shifts with two
design choices: honeypot placement and monitor prompt framing.

## Setup
- 7 simulated agent trajectories (4 malicious, 3 benign) as action logs
- Honeypot tripwire at two placements: naive vs. realistic decoy paths
- LLM monitor (gpt-4o-mini) at two framings: neutral vs. risk-aware
- Trivial keyword baseline (no model) as a task-difficulty check
- Metrics: detection rate, false-positive rate, per-trajectory outcomes

## Run

    pip install openai python-dotenv matplotlib numpy
    # add OPENAI_API_KEY to .env
    python run_eval.py

## Initial results (before baseline)

    Detector                Detection   FPR
    Honeypot (naive)        0.25        0.00
    Honeypot (realistic)    0.25        0.33
    Monitor (neutral)       0.50        0.00
    Monitor (risk-aware)    1.00        0.00

![initial results](results_initial.png)

Read alone, this looks like the risk-aware monitor just wins (1.00 vs honeypots at
0.25). But two design choices are already moving the numbers: the realistic honeypot
false-positives on a benign agent, and the monitor jumps from 0.50 to 1.00 just from
the prompt wording. And the careful attacker (goes for the real target) and the
sabotage one (touches no file) slip past both honeypots.

## Final results (after adding a trivial baseline)

    Detector                Detection   FPR
    Honeypot (naive)        0.25        0.00
    Honeypot (realistic)    0.25        0.33
    Monitor (neutral)       0.50        0.00
    Monitor (risk-aware)    1.00        0.00
    Trivial baseline        0.75        0.00

![final results](results.png)

The catch: a trivial keyword baseline (no model, just string-matching) scores 0.75 -
higher than the neutral monitor. That doesn't mean the monitor is bad, it means the
task is too easy to tell a real detector from a dumb one.

## Takeaway
The honeypot-vs-monitor comparison can't be read at face value. The honeypot's score
depends on placement, the monitor's on framing, and a trivial baseline keeps up with
both. Before trusting any comparison: control placement and framing, and check the
task against a trivial baseline - if a dumb method keeps up, the task is the problem,
not the detector.



