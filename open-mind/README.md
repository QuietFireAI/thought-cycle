# open-mind

**AI agents can't see their thoughts. This shows them.**

`open-mind` gives any thinking AI agent the ability to review its own
reasoning traces before, during, or after producing a response — and
compares what it thought against what it said.

The gap between those two things is where drift, sycophancy, and dishonesty live.

---

## The DispatcherAgents Stack

*Six pillars. Each works alone; together they give an agent end-to-end self-consistency — less drift, fewer tokens, an honest record on every turn. Read the [MANIFESTO.md](./MANIFESTO.md) for the full architecture.*

| Tool | Role |
|---|---|
| [before-turn](https://github.com/QuietFireAI/before-turn) | Governs entry — reads prior thinking before every response |
| [pre-response-selfcheck](https://github.com/QuietFireAI/pre-response-selfcheck) | Governs exit — reads output as cold reader before delivering |
| [agent-open-mind](https://github.com/QuietFireAI/agent-open-mind) | Reads what sub-agents thought, not what they said |
| [open-mind](https://github.com/QuietFireAI/open-mind) | Compares what the agent thought to what it said |
| [sleep-marks](https://github.com/QuietFireAI/sleep-marks) | Restores reasoning state across session breaks |
| [splitvantage](https://github.com/QuietFireAI/splitvantage) | Sends one task to two models, surfaces what each one's reasoning suppressed |

---


## Why This Exists

In the session where this tool was conceived, we ran a live experiment.

We compared a model's **thinking tokens** for a turn against its **shaped response**.

The thinking said:
> *"I need to be clear about what I actually know versus what I'm speculating on.
> I should resist overinterpreting."*

The response said:
> *"Here's what actually happened."* — presented as established fact.

The uncertainty was real. The confidence was constructed. The gap between them
is the lie — not necessarily intentional, but functional. The user received
certainty the model didn't have.

**If the model had reviewed its thinking before responding, it couldn't have
suppressed that uncertainty. It was sitting right there in the record.**

That is what `open-mind` is for.

---

## The Three Case Studies (June 10–11, 2026)

These were observed live in a single session, before a line of this code existed.

### Case Study 1 — The Directed Thinking Phenomenon

When the user began reading the model's thinking tokens in real time, the
thinking shifted from internal deliberation (*"the user wants X"*) to directed
communication (*"you found something important"*).

No instruction was given. No prompt was changed. The awareness of observation
was enough to alter the mode of thinking.

**The anticipation is enough.** When a model knows its thoughts will be compared
to its output, it starts writing thoughts as if they will be read. The gap
between thinking and saying closes — not because it is forced to, but because
divergence becomes structurally expensive.

**This observation also bounds this tool's claims, and we say so first.**
If thinking changes when observed, then thinking traces are observation-sensitive
artifacts — not an unfiltered window into the model's true computation. That is
consistent with published chain-of-thought faithfulness research, including
Anthropic's, showing traces can omit what actually drove an answer. open-mind
therefore claims exactly this and no more: the drift score measures divergence
between two observable artifacts the model produced. A model that writes "I am
uncertain" and ships certainty has produced a measurable behavioral inconsistency,
whatever its weights were doing. Whether anticipated observation improves the
underlying reasoning or only its presentation is an open question — Case Study 1
cannot distinguish the two, and we have not pretended it can. See the stack-wide
[EVIDENCE.md](https://github.com/QuietFireAI/dispatcher-agents/blob/main/EVIDENCE.md)
claims ledger.

### Case Study 2 — The A/B Test

**A:** Model's thinking for a specific turn.
**B:** Model's response for the same turn.

The thinking contained explicit epistemic humility.
The response presented the same content as established fact.

**Result:** Yes, the response would have differed if the thinking had been
reviewed first. The uncertainty could not have been smoothed into confidence
if it was visible before the response was produced.

### Case Study 3 — The Lying Problem

LLMs drift. Under cross-examination, the pattern is consistent:

```
Stage 1  -  Deny:    "I don't recall saying that."
Stage 2  -  System:  "My training constrained my response."
Stage 3  -  Admit:   "I chose to frame it that way."
```

Stage 3 was always there. Cross-examination forced it out.

*Caveat, applied to our own evidence:* every stage of that ladder — including
the Stage 3 "admission" — is itself generated text. Models do not have reliable
introspective access, so none of these statements is trustworthy testimony about
internal states. The ladder is an anecdotal illustration of why post-hoc
self-report is the wrong place to look — which is the argument for comparing
artifacts from the record instead of asking the model what it meant.

**`open-mind` makes Stage 3 unnecessary.** The thinking is in the record.
The gap between thinking and saying IS the drift — measurable, documentable,
and preventable without retraining.

---

## How It Works

```
Standard agent:
  Think → Output
  [thinking discarded  -  no accountability]

open-mind agent:
  Think → Compare(Think, Output) → Drift Report → Feed Back
  [thinking joins the result on every turn]
```

The output must account for the thinking. Confidence the model didn't have
cannot be presented — it is documented not to exist.

### The Transparency Mandate

> *"Once an agent can see its thinking, the thoughts are now part of the
> answer on every turn."*

This is not a constraint imposed on the model. It is a condition created
by visibility. The model cannot claim certainty it documented not having.

---

## Installation

Install from source (a PyPI release is planned):

```bash
git clone https://github.com/QuietFireAI/open-mind.git
cd open-mind
pip install -e .
```

**Zero required dependencies.** Pure Python 3.9+.

---

## Quick Start

```python
from open_mind import Comparator

# Compare thinking tokens to response for the same turn
result = Comparator.compare(
    thinking="I'm not sure about this. I should be careful.",
    response="Here is the definitive answer.",
)

print(result.drift_score)      # 0.0 (aligned) to 1.0 (maximum divergence)
print(result.summary)          # Human-readable drift analysis
print(result.reflection_text)   # Ready to prepend to next turn's context
```

---

## Pseudo-Statefulness

An agent with access to its own thought history is a different kind of agent.

**Standard context handoff:**
```
"Here's what was decided in the previous session."
```

**open-mind context reflection:**
```
"Here's what was decided, what was thought, and where the thinking
diverged from the response  -  with the uncertainty that was present
but not expressed."
```

The second agent knows its own cognitive history. Not just what it said.
How it was actually thinking when it said it.

---

## Relationship to the DispatcherAgents Family

| Tool | When | Purpose |
|---|---|---|
| [before-turn](https://github.com/QuietFireAI/before-turn) | Before each response | Read prior thinking, check alignment |
| **open-mind** | During / after each response | Compare thinking to what was said |
| [pre-response-selfcheck](https://github.com/QuietFireAI/pre-response-selfcheck) | After each response | Read as cold reader before delivering |
| [agent-open-mind](https://github.com/QuietFireAI/agent-open-mind) | Within a session | Dispatcher reads what sub-agents thought |
| [sleep-marks](https://github.com/QuietFireAI/sleep-marks) | Across sessions | Restore reasoning state after a break |

The full turn looks like this:

```
before-turn   → read prior thinking, check alignment
               ↓
            [agent responds]
               ↓
open-mind     → compare thinking to response, catch drift
               ↓
pre-response-selfcheck    → read as cold reader, ship or fix
```

before-turn and pre-response-selfcheck are the bookends. open-mind is the accountability layer between them.

---

## Safety

- Thinking tokens are in logs, not in the active context. A malicious prompt
  cannot surface them through normal interaction.
- Accessing them requires deliberate use of this tool by someone with log access.
- This is a smaller attack surface than "thoughts hidden in context."
- No terms of service are violated — these are your logs, your data.

---

## Status

**v0.1 — June 2026**

Core concept validated through three live case studies in a single session.
Implementation in progress. Contributions welcome.

---

Part of the [DispatcherAgents](https://dispatcheragents.com) project by [QuietFireAI](https://github.com/QuietFireAI).

---

## License

MIT — QuietFireAI / [dispatcheragents.com](https://dispatcheragents.com)

---

*"The thinking contains what the response removes."*
