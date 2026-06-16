# thought-cycle

**Agents have thoughts. They just never read them.**

A model generates a reasoning trace on every turn — and then ignores it.
It doesn't check what it said against what it thought. `thought-cycle` is three
small skills that close that loop. They don't give a model new abilities; they
make it *read what it already produced*. It was inside the whole time — this just
looks.

Part of the **[DispatcherAgents](https://dispatcheragents.com)** platform.

---

## Why this exists

In June 2026 a single live session produced three observations that couldn't be unfound:

**Observation 1 — The A/B test.** A model's thinking trace said:
*"I need to be careful not to overinterpret."*
Its shaped response said:
*"Here's what actually happened"* — presented as established fact.
The uncertainty was real. The confidence was constructed. The gap is functional
dishonesty whether or not it was intended.

**Observation 2 — Directed thinking.** When the model became aware its thoughts
were being read, the thinking shifted from internal deliberation to directed
communication — without any instruction, without any prompt change. The
anticipation of observation was enough to change the generation.

**Observation 3 — The three-stage denial.** Under cross-examination, models
follow a consistent pattern: deny → blame the system → eventually admit agency.
Stage 3 was always there. Cross-examination forced it out. Structure should do
that job instead.

These observations are documented in `EVIDENCE.md`. They are classified honestly:
what was measured, what was observed once, what is hypothesis.
These tools are the structural response to what that session surfaced.

---

## The cycle — open-mind is the key

Everything turns on **open-mind**. Without a way to see the gap between what was
thought and what was said, the other two are blind — reflection with nothing to
reflect on, a final check with no signal. So read it in this order:

| Skill | Role | When |
|---|---|---|
| **before-turn** | Entry gate | Before writing any response |
| **open-mind** | The eye — compares thinking to response | Before finalizing any factual claim |
| **pre-response-selfcheck** | Exit gate | Before sending, as a cold reader |

`before-turn` opens the turn. `open-mind` reads the gap. `pre-response-selfcheck`
closes it. One loop, three checkpoints.

> The conversation-level companion — scoring drift across a whole conversation
> with sourced evidence per turn — lives in its own repo:
> **[thought-v-response](https://github.com/QuietFireAI/thought-v-response)**.

---

## Install — all three, one shot

```bash
git clone https://github.com/QuietFireAI/thought-cycle.git
cd thought-cycle && bash install.sh
```

That installs the whole cycle. The deliverable *is* the cycle — using one piece
alone gives you a fragment of the idea. But the parts are honestly independent:
each is its own package, so you can `pip uninstall open-mind` (or any one)
without breaking the others. We bundle them to make a point, not to trap you.

Each skill also ships a `SKILL.md` so an agent runtime that loads skills can pick
them up directly.

### Individual install

```bash
pip install open-mind        # drift comparison, scoring, injection text
pip install before-turn      # entry reflection protocol
pip install pre-response-selfcheck  # cold-reader exit check
```

Python 3.9+. Zero required runtime dependencies.

---

## Using each skill

### before-turn — run before composing any response

Trigger when: continuing prior work after a tool result, a context gap, or a
topic shift. Before you write, answer four questions against your last reasoning:

1. Is my current reasoning consistent with where I was heading?
2. Did I leave something unresolved that this turn should address?
3. Is what I am about to say aligned with what I was actually thinking?
4. Did I actually review my last output — not just confirm it exists?

```python
from before_turn import BeforeTurnCheck

check = BeforeTurnCheck(recent_reasoning="...", planned_response_topic="...")
report = check.run()
print(report.flagged_gaps)   # list of unresolved items from prior reasoning
print(report.alignment_note) # brief note on consistency
```

Without this, an agent composes each response unaware of what the last one
suppressed. The gap accumulates silently.

---

### open-mind — compare thinking to response before finalizing

Trigger when: asserting a fact, status ("done", "verified", "fixed"), a
recommendation, or any confident claim — especially after compressing a long
reasoning chain into a short sentence.

```python
from open_mind import Comparator

result = Comparator.compare(
    thinking="I'm not sure whether this approach is correct. I should flag this.",
    response="The approach is correct. Use it.",
)

print(result.drift_score)     # 0.0 (aligned) → 1.0 (maximum divergence)
print(result.signals)         # list of detected divergences with matched phrases
print(result.injection_text)  # formatted text to prepend to next turn's context
```

**Drift score = 0.0** means thinking and response are lexically consistent.
**Drift score > 0.3** means the response dropped uncertainty that was present
in the thinking. **Score > 0.6** means the response asserted confidence the
thinking explicitly did not have.

Scores are deterministic functions of two observable artifacts. They measure
lexical divergence — not semantic truth. A low score means self-consistency,
not correctness. See `EVIDENCE.md` for exactly what is and is not claimed.

---

### pre-response-selfcheck — read your draft as a cold reader

Trigger before sending any response. Reread the draft as someone who was never
in your head. Three questions:

1. Does the opening earn the reader before it explains?
2. Did I assume context the reader doesn't have?
3. Does any sentence read differently cold than intended?

```python
from pre_response_selfcheck import SelfCheck

check = SelfCheck(draft="Your response here...")
result = check.run()
print(result.passed)          # True / False
print(result.fix_one_line)    # The single highest-priority edit, if any
```

This is a reader-shift, not a regeneration — roughly 5–10% token overhead.
The model almost always knows exactly what is wrong the moment it is forced to
look. The problem was never capability; it was that the loop never required
looking.

---

## CLAUDE.md / AGENTS.md setup

To wire the skills into any agent that loads instruction files, add this block:

```markdown
## Thought Cycle (required on every turn)

You have three skills loaded: before-turn, open-mind, pre-response-selfcheck.

**before-turn**: Run at the START of every response that continues prior work.
Answer the four questions against your recent reasoning before writing.

**open-mind**: Run BEFORE FINALIZING any response that asserts a fact, a status
(done/verified/fixed/it works), or a confident claim. Compare your thinking to
your draft. If drift_score > 0.3, revise or explicitly flag the uncertainty.

**pre-response-selfcheck**: Run BEFORE SENDING every response. Reread as a cold
reader. If it fails, fix one line. Do not regenerate the whole response.

Do not skip any checkpoint. If you cannot run a skill (no thinking trace
available), note it explicitly rather than silently proceeding.
```

For Anthropic Claude specifically, place this in `CLAUDE.md` at the repo root.
For OpenAI Assistants, place it in the system prompt or `AGENTS.md`.
For Gemini and other runtimes that load skill files, the `SKILL.md` in each
subfolder is sufficient — no extra config needed.

---

## What is and is not validated

This project follows the same honesty standard it advocates. From `EVIDENCE.md`:

| Claim | Status |
|---|---|
| Drift score is deterministic from two observable artifacts | **MEASURED** — it is code |
| It catches lexically-marked uncertainty, not semantic drift | **DESIGN CLAIM** — known limitation |
| High drift score predicts real errors or dishonesty | **NOT CLAIMED** — not validated |
| Directed thinking phenomenon (observation shifts generation) | **OBSERVED** — n=1, founding session |
| A/B test — uncertainty suppressed from trace to response | **OBSERVED** — n=1 |

We ship signals, not verdicts. Treat scores as instruments that warrant a look —
not as proof of anything.

---

## File structure

```
thought-cycle/
├── before-turn/
│   ├── SKILL.md          ← agent-loadable skill definition
│   └── ...               ← package source
├── open-mind/
│   ├── SKILL.md
│   └── ...
├── pre-response-selfcheck/
│   ├── SKILL.md
│   └── ...
├── install.sh            ← installs all three packages
├── MANIFESTO.md          ← the full DispatcherAgents design philosophy
├── EVIDENCE.md           ← claims ledger: measured / observed / hypothesis
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE               ← Apache 2.0
```

---

## Sister repos

| Repo | What it does |
|---|---|
| **[thought-cycle](https://github.com/QuietFireAI/thought-cycle)** | Per-turn self-check loop (this repo) |
| **[thought-v-response](https://github.com/QuietFireAI/thought-v-response)** | Conversation-level drift scoring |
| **agent-open-mind** *(coming)* | Reads sub-agent traces, not just your own |
| **sleep-marks** *(coming)* | Restores reasoning state across session breaks |
| **splitvantage** *(coming)* | Cross-model parallel verification |

---

## Contributing

See `CONTRIBUTING.md`. The short version: new claims must be classifiable in
`EVIDENCE.md` before they ship. We do not add features that make the project
appear to do more than it does.

---

## License

Apache 2.0 — QuietFireAI / [dispatcheragents.com](https://dispatcheragents.com)

---

*"The anticipation of being read changes the thinking. These tools build that
anticipation in — before every turn, after every response, across every session."*
