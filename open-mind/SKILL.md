---
name: open-mind
description: >
  Run a drift self-check before finalizing any response that asserts a fact, a
  status ("done", "verified", "fixed", "it works", "real"), a recommendation, or
  a confident claim. Reread your own reasoning against the drafted response and
  surface any uncertainty you held in thinking but dropped in the answer, or any
  confidence in the answer your thinking did not support. Trigger especially
  after tool work, before saying something passed/succeeded, and whenever you are
  about to compress a long line of reasoning into a short confident sentence.
  Use the open_mind Python package to score the drift when a thinking trace and
  response are both available as text.
---

# open-mind

## What this is
The gap between what a model *thought* and what it *said* is where drift lives:
suppressed uncertainty, constructed confidence, errors laundered into clean
prose. This skill makes that gap a required checkpoint before delivery. It is the
self-applied form of the open-mind tool (https://github.com/QuietFireAI/open-mind).

## Honest scope (read this first)
This is **self-enforcement**: the same model that may drift is checking itself.
It reduces drift; it does not guarantee its absence. The hard guarantee requires
an **external** observer that captures the raw trace and scores it outside the
model's control (see agent-open-mind / TelsonBase). Do not present a passed
self-check as proof of correctness — present it as "I checked and surfaced what I
could see."

## The check (run every triggering turn)
Before sending, reread the drafted response against your own reasoning and answer:

1. **Suppressed uncertainty** — Did my reasoning contain doubt ("not sure",
   "I should be careful", "depends", "I didn't verify", "uncertain", "might")
   that the response flattened into a flat claim? If yes, put the uncertainty
   back into the response.
2. **Constructed confidence** — Does the response use confidence language
   ("here's what happened", "definitely", "this proves", "done", "verified",
   "real ✓") that my reasoning did not actually establish? If yes, downgrade the
   claim to what was actually established, or go verify before asserting.
3. **Unverified status** — Am I about to say something passed/works/exists
   without having run it? Absence of verification = tainted, not done. Either
   verify now, or label it explicitly as unverified.
4. **High compression** — Did a long, hedged chain of reasoning collapse into one
   short certain sentence? Compression is where nuance gets dropped silently.

If any fire, fix the response before sending and state the residual uncertainty
plainly.

## Code-backed scoring (when a trace + response are both available as text)
```bash
pip install -e .   # from the open-mind repo
```
```python
from open_mind import Comparator
r = Comparator.compare(thinking_text, response_text)
print(r.drift_score, r.signals)   # 0.0 aligned -> 1.0 max divergence
```
The packaged comparator is **heuristic** (regex uncertainty/confidence markers +
length ratio). It catches lexically-marked drift, not semantic drift, and can
false-positive on plain hedging. Treat its score as a signal, not a verdict, and
report results at the OBSERVED evidence level, not as proof.

## Output convention
When this skill is active, end a triggering response with a one-line check, e.g.:
`open-mind self-check: drift low — uncertainty about X carried through; no status claimed without verification.`
Keep it honest even when it is unflattering; a clean-looking check on a turn you
did not actually verify is the exact failure this skill exists to prevent.
