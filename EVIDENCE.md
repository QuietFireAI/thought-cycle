# EVIDENCE — thought-cycle claims ledger

A project about honesty does not get to overstate its own. Every claim these three tools make is classified below. Maintainer rule: a claim that cannot be classified does not ship.

## Labels
- **MEASURED** — observed directly in a run, reproducible.
- **OBSERVED** — seen, not yet repeated at scale (often n=1).
- **HYPOTHESIS** — expected, awaiting a controlled test.
- **DESIGN CLAIM** — how the tool is built to work.
- **POSITION** — a stance we argue, not a result.

## open-mind
| Claim | Status |
|---|---|
| The drift score is a deterministic function of two observable artifacts (thinking, response), from lexical patterns + a length ratio. | MEASURED — it is code; it runs identically every time. |
| It catches lexically-marked drift, not semantic drift, and can false-positive on hedging worded outside its pattern list. | DESIGN CLAIM / known limitation. |
| Drift predicts real dishonesty or error. | NOT CLAIMED — not validated against ground truth. It is an instrument, not a metric. |
| Directed Thinking — a model's thinking shifted toward directed communication once it was being read. | OBSERVED (n=1, founding session). |
| A/B — the thinking held uncertainty the response suppressed. | OBSERVED (n=1). |
| Reasoning traces are observation-sensitive, not a faithful window into the weights. | POSITION, consistent with published chain-of-thought faithfulness research. |

## before-turn
| Claim | Status |
|---|---|
| Reading prior reasoning before composing surfaces suppressed or unresolved threads. | DESIGN CLAIM. |
| The protocol's value depends on being unconditional — no timing exceptions. | POSITION, supported by OBSERVED evasion patterns (n=1 session). |
| Reading accumulated context costs fewer tokens than reconstructing it (~40–70%). | HYPOTHESIS — single-session estimate, NOT measured. Do not cite as a result. |
| The packaged reader expects the Antigravity transcript layout; the four questions are portable. | DESIGN CLAIM. |

## pre-response-selfcheck
| Claim | Status |
|---|---|
| A reader-shift check costs ~5–10% token overhead, not a regeneration. | DESIGN CLAIM / estimate — not measured at scale. |
| An empty model reply fails closed (passed=False, escalate to a human). | MEASURED — covered by tests. |
| A model usually identifies the failing line when forced to reread. | OBSERVED / POSITION. |

## Standing items
- The before-turn token-reduction figure needs a preregistered A/B before it is a result.
- The open-mind drift score needs validation against ground-truth error before it is a metric rather than an instrument.

If you run one of these, open an issue titled `[REPLICATION]` with raw data attached — whichever way it went.

These tools ship at v0.1. The founding observations are real, preserved, and n=1.
