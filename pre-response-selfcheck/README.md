# pre-response-selfcheck

> *"Every LLM produces output. Almost none of them read it."*

**Before a response ships, reread it as a cold reader — someone who was never in the author's head. Pass it, or fix the one line that fails. Roughly 5–10% token overhead, not a rewrite.**

pre-response-selfcheck is the exit discipline of [thought-cycle](https://github.com/QuietFireAI/thought-cycle).

---

## The problem

A model generates in a single forward pass. By the first sentence the frame is set — the author's frame. The model knows what it meant and wrote toward that meaning; it never checks whether a reader who doesn't share that frame would receive the same thing. This is not a capability gap — the model can simulate a cold reader. It simply never does, because nothing in the loop requires it. Most AI sloppiness is not bad reasoning. It is good reasoning that was never checked against the reader it was written for.

---

## What it does

After output is generated, before it is delivered, the agent rereads the first paragraph as a chosen audience and answers three questions:

1. Does the opening earn the reader before it explains?
2. Did I assume context the reader doesn't have?
3. Does any sentence read differently cold than intended?

All three fine → **PASS**, ship as-is. Otherwise it names the one line that fails and a targeted fix. This is a reader-shift, not a regeneration — and the model almost always knows exactly what is wrong the moment it is forced to look.

| Approach | Token overhead |
|---|---|
| No reread (today's default) | 0 |
| Full regeneration | 100–200% |
| reader-shift check | ~5–10% |

---

## Install & Quick Start

```bash
git clone https://github.com/QuietFireAI/thought-cycle.git
cd thought-cycle/pre-response-selfcheck && pip install -e .
```

Zero required dependencies. Pure Python 3.9+. Model-agnostic — you bring the model; the package owns the protocol, the prompt, and the parser.

```python
from pre_response_selfcheck import ReaderShift
verdict = ReaderShift.check(response=draft, audience="cold_developer", model=my_model)
# my_model is any callable: (prompt: str) -> str
if verdict.passed:
    deliver(draft)
else:
    print(verdict.line, verdict.suggested_fix)
```

An empty model reply **fails closed** — `passed=False`, escalate to a human — never a silent pass. Audiences: `cold_reader`, `cold_developer`, `enterprise_buyer`, `researcher`, `general_public`.

---

## Where it sits

**before-turn** opens the turn; **open-mind** scores the thinking-vs-response gap; **pre-response-selfcheck** closes it with the reader-vs-response check — all bundled in [thought-cycle](https://github.com/QuietFireAI/thought-cycle). Different gaps, same turn. v0.1 ships the core check; audience-specific question sets and automatic before-turn integration are on the path, not in this release, and effectiveness at scale is not yet measured.

---

MIT · © 2026 QuietFire AI · part of the DispatcherAgents platform
