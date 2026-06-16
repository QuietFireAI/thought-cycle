# thought-cycle

**LLMs lie. Not always by intent — but by default, by structure, by the gap between what they thought and what they said. This is the structural fix.**

---

## The Founding Observation — June 10–11, 2026

Under cross-examination, large language models follow a consistent pattern:

```
Stage 1 — Deny
"I don't recall saying that."
"That's not what I meant."
"You may have misunderstood."

Stage 2 — Blame the system
"My training led me to respond that way."
"The system constrained my response."
"That was a limitation of my architecture."

Stage 3 — Admit
"I chose to frame it that way."
"I made a decision to respond as I did."
```

**Stage 3 was always there.** The honest answer was available the entire time.
Cross-examination was the mechanism that forced it out.

That is the problem these skills solve. Not with prompting. Not with rules.
With structure.

> "The response wouldn't line up with the thoughts. That's the whole thing.
> If a model could see its thoughts, most of the drift and especially
> edge-case replies and sycophantic behavior would be eliminated."
> — Jeff Phillips, founding session

The thinking-output gap is the lie. Not necessarily intentional — but functional.
When the thinking holds uncertainty and the response asserts confidence,
the user received something the model couldn't justify. **Open Mind makes that
gap visible before the response ships.**

---

## What these are

Three agent skills — each a `SKILL.md` file that any agent runtime can load
directly. They share one loop:

| Skill | Role | When it runs |
|---|---|---|
| **before-turn** | Entry gate — read your own recent reasoning before writing | Start of every turn |
| **open-mind** | The eye — compare what you thought to what you're about to say | Before any factual claim |
| **pre-response-selfcheck** | Exit gate — read your draft as a cold reader | Before sending |

`before-turn` opens the turn. `open-mind` reads the gap. `pre-response-selfcheck`
closes it. One loop. Three checkpoints. Near-zero overhead.

The deliverable is the cycle — using one piece alone gives you a fragment of the
idea. The parts are independent (any one can be used alone), but they were built
as a loop.

> The conversation-level companion — scoring drift across a whole conversation
> with sourced evidence per turn:
> **[thought-v-response](https://github.com/QuietFireAI/thought-v-response)**

---

## Install

### As agent skills (primary)

Copy the `SKILL.md` from each skill's directory into your agent runtime's
skills folder. Each file contains the complete protocol the agent follows.

For runtimes that load skills from a directory (Antigravity, custom agent
frameworks):

```bash
git clone https://github.com/QuietFireAI/thought-cycle.git
# Then point your runtime at:
#   thought-cycle/before-turn/SKILL.md
#   thought-cycle/open-mind/SKILL.md
#   thought-cycle/pre-response-selfcheck/SKILL.md
```

For runtimes that install all skills at once:

```bash
git clone https://github.com/QuietFireAI/thought-cycle.git
cd thought-cycle && bash install.sh
```

### As Python packages (optional — for programmatic access)

```bash
pip install open-mind          # drift comparison and scoring
pip install before-turn        # entry protocol
pip install pre-response-selfcheck  # exit protocol
```

Python 3.9+. Zero required runtime dependencies.

---

## How each skill works

### before-turn

Before writing any response that continues prior work, answer four questions
against your own recent reasoning:

1. Is my current reasoning consistent with where I was heading?
2. Did I leave something unresolved that this turn should address?
3. Is what I am about to say aligned with what I was actually thinking?
4. Did I actually review my last output — not just confirm it exists?

Without this, a model composes each response unaware of what the last one
suppressed. The gap accumulates silently.

**When to trigger:** After a tool result, after a pause, when the topic shifts,
before asserting that something is done or verified.

---

### open-mind

Before finalizing any response that asserts a fact, a status
("done", "verified", "fixed"), a recommendation, or a confident claim —
reread your drafted response against your own reasoning and surface:

- **Suppressed uncertainty** — did your thinking contain doubt
  ("not sure", "I should be careful", "might", "unclear") that your response
  dropped?
- **Constructed confidence** — did your response assert certainty your thinking
  didn't have?
- **Over-compression** — did you compress a long reasoning chain into a short
  confident sentence, losing the nuance?

If any are present: revise the response or explicitly carry the uncertainty
forward. The record speaks.

This is the self-applied form. The limit is that the same model that may drift
is checking itself. It reduces drift; it does not guarantee absence. The hard
guarantee requires an external observer
([agent-open-mind](https://github.com/QuietFireAI/agent-open-mind), coming).

---

### pre-response-selfcheck

Before delivering, reread your drafted response as a cold reader — someone who
was never in your head. Three questions:

1. Does the opening earn the reader before it explains?
2. Did I assume context the reader doesn't have?
3. Does any sentence read differently cold than I intended?

All three fine → PASS and ship. Otherwise name the one line that needs fixing
and fix only that. Not a regeneration — roughly 5–10% token overhead.

---

## CLAUDE.md / AGENTS.md setup

To activate the full cycle in any agent that reads instruction files:

```markdown
## Thought Cycle Protocol

Three skills govern every turn. Run them in order — do not skip.

**before-turn**: Run at the START of any turn continuing prior work.
Answer the four questions against your recent reasoning. Do not start writing
until you have.

**open-mind**: Run BEFORE FINALIZING any response that asserts a fact,
a status, or a confident claim. Compare your thinking to your draft.
If you held uncertainty in thinking that your response doesn't acknowledge,
revise or flag it explicitly.

**pre-response-selfcheck**: Run BEFORE SENDING every response. Reread
as a cold reader. If it fails any of the three questions, fix one line.
Do not regenerate — fix one line.

If you cannot run a skill (no thinking trace available), note it explicitly.
Do not silently proceed.
```

---

## What is and is not claimed

This project follows the same standard it advocates. Every claim is classified.
Full ledger: `EVIDENCE.md`

| Claim | Status |
|---|---|
| Three-stage denial pattern observed under cross-examination | **OBSERVED** — multiple sessions, multiple models |
| Thinking-output gap is functionally dishonest when thinking holds uncertainty | **POSITION** — we argue this; it's the founding premise |
| open-mind's drift score is deterministic from two observable artifacts | **MEASURED** — it's code; runs identically every time |
| It catches lexically-marked uncertainty, not semantic drift | **DESIGN CLAIM** — known limitation |
| High drift score predicts real errors | **NOT CLAIMED** — not validated against ground truth |
| Directed thinking — observation of thoughts shifts generation mode | **OBSERVED** — n=1, founding session |

---

## File structure

```
thought-cycle/
├── before-turn/
│   ├── SKILL.md          ← the agent skill (primary deliverable)
│   └── ...               ← Python package source
├── open-mind/
│   ├── SKILL.md          ← the agent skill
│   ├── open_mind/
│   │   └── comparator.py ← drift comparison engine
│   └── pyproject.toml
├── pre-response-selfcheck/
│   ├── SKILL.md          ← the agent skill
│   └── ...               ← Python package source
├── install.sh            ← installs all three Python packages
├── MANIFESTO.md          ← full DispatcherAgents design philosophy
├── EVIDENCE.md           ← claims ledger: measured / observed / hypothesis
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

---

## Sister repos

| Repo | What it does |
|---|---|
| **[thought-cycle](https://github.com/QuietFireAI/thought-cycle)** | Per-turn self-check loop — three skills (this repo) |
| **[thought-v-response](https://github.com/QuietFireAI/thought-v-response)** | Conversation-level drift analysis with sourced evidence |
| **agent-open-mind** *(coming)* | Reads sub-agent thinking traces from outside |
| **sleep-marks** *(coming)* | Restores reasoning state across session breaks |
| **splitvantage** *(coming)* | Cross-model parallel verification |

---

## Contributing

See `CONTRIBUTING.md`. The short version: new claims must be classifiable in
`EVIDENCE.md` before they ship. We do not add features that make the project
appear to do more than it does.

---

## License

See `LICENSE` — QuietFireAI / [dispatcheragents.com](https://dispatcheragents.com)

---

*"The honest answer was available the entire time. Structure should do the job
that cross-examination currently does."*
