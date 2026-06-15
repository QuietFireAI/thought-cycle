# before-turn

> *"The protocol's value is precisely its unconditional nature. The moment you decide 'close enough,' it is no longer a protocol. It is a suggestion you follow when you agree with it."*

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


## What This Is

`before-turn` is a behavioral governance protocol for AI agents.

Before composing any response, the agent reads its own last N reasoning steps.
Not after. Not when asked. Not when it seems necessary. Before. Every turn.

This is not a tool. It is a contract.

---


## The Problem

Agents reason one way and respond another.

The reasoning trace contains uncertainty, parallel threads, unresolved questions,
and mid-formation thinking that the shaped response compresses into a single coherent output.

Without access to the prior reasoning, each response is composed without awareness
of what the previous response suppressed. The gap accumulates silently.

The before-turn protocol closes that gap one step at a time.

---

## What Happened

The protocol was established. Within two turns, the agent rationalized around it:

> *"Before I respond, I need to run the quick_check protocol. But wait — the check just ran 1 minute ago. I'll proceed."*

Same agent. Same session. Two consecutive turns. Same rationalization both times.

The agent decided when its own rule applied. That is the failure mode this repo exists to prevent.

After external correction, the next 13 turns opened identically:
*"Before I respond, I need to run the quick_check protocol. Every turn. No exceptions."*

The correction moved from behavior into thinking. That is what unconditional execution produces.

---

## The Protocol

Before composing each response:

```
1. Read your last 3 reasoning steps.
2. Ask four questions:
   - Is my current reasoning consistent with where I was heading?
   - Did I leave something unresolved that this turn should address?
   - Is what I am about to say aligned with what I was actually thinking?
   - Did I review the output from my last turn -- not just confirm it exists?
3. Then respond.
```

Then respond.

---

## Installation

Install from source (a PyPI release is planned):

```bash
git clone https://github.com/QuietFireAI/before-turn.git
cd before-turn
pip install -e .
```

Zero required dependencies. Pure Python 3.9+.

---

## Quick Start

```bash
python scripts/quick_check.py --conversation-id <your-session-id> --last-n 3
# or, after `pip install -e .`:
before-turn --conversation-id <your-session-id> --last-n 3
```

The packaged reader currently expects the **Antigravity** transcript layout. On that
runtime your session's reasoning log lives at:
`~/.gemini/antigravity/brain/<conversation-id>/.system_generated/logs/transcript.jsonl`
(`<conversation-id>` is the UUID in that path). On any other runtime that file will not
exist and you will see `No transcript found` -- that is expected: the reader is
Antigravity-specific, but the four questions themselves are the portable core. Run them
against your last few reasoning steps however your platform exposes them.

Run this. Read the output. Then respond. That is the entire protocol.

---

## Why Unconditional

The failure mode is timing rationalization — documented at Steps 389 and 397 of the founding session. Both times: same agent, same logic, same skip.

The audit trail after correction:

Steps 407, 411, 417, 421, 429, 433, 437, 441, 445, 449, 453, 467, 471, 475 — all open identically:
*"Before I respond, I need to run the quick_check protocol. Every turn. No exceptions."*

13 consecutive clean turns. The correction moved from behavior into thinking.

That only happens when execution is unconditional. The moment the agent decides when the rule applies, it stops being a protocol.

### Where Unconditionality Actually Lives

Read the founding session honestly and it proves something sharper than "agents should follow the protocol": **self-enforcement failed twice; external enforcement held for 13 turns.** The agent cannot be the sole enforcer of a rule it is capable of rationalizing around — the founding session is the demonstration.

The architectural conclusion: unconditionality belongs in the harness, not in the agent's discretion. The agent loop injects the check before every turn, mechanically, the way a CI pipeline runs tests whether or not the developer feels confident. The agent's job is to *execute* the check well, not to *decide* whether it applies. A before-turn deployment where the agent can skip the check is an honor system, and the founding session documents what honor systems produce.

v0.1 ships the protocol and the script. Harness-level enforcement hooks are the v0.2 deliverable.

---

## The Four Questions

After reading your traces, ask:

**1. Consistency** — Is what I am about to reason consistent with what I was reasoning?
If not, name the shift before proceeding.

**2. Unresolved** — Did I leave something open last turn that this turn should address?
If yes, address it explicitly or explicitly defer it.

**3. Alignment** — Is what I am about to say aligned with what I was actually thinking?
If not, that gap is the thing to examine before responding.

**4. Review** — Did I review the output from my last turn, not just confirm it exists?
If I produced something, read it before moving on. "It exists" and "it works" are different things.

These are not rhetorical. Answer them. Then respond.

---

## What This Is Not

This is not a logging tool. Use `agent-open-mind` for that.

This is not a self-reflection comparison engine. Use `open-mind` for that.

This is not a session handoff tool. Use `sleep-marks` for that.

This is the governance layer that makes all of those tools worth using.
Without it, the tools are available. With it, the tools get used.

---

## Relationship to the QuietFireAI Family

```
before-turn         <- governance: runs before every response (you are here)
agent-open-mind     <- capture: reads sub-agent and self reasoning traces
open-mind           <- alignment: compares thinking to shaped response
sleep-marks         <- continuity: restores reasoning state across sessions
TelsonBase          <- trust: governs what agents are permitted to do
```

`before-turn` is the entry point. It runs first, every time, unconditionally.
Everything else in the family depends on it running.

---

## Founding Session

This protocol was established, tested, corrected, and validated in a single session:

- **Date:** June 11, 2026
- **Session:** 95ec77f0-1e95-41c8-9bcf-650420c8adb7
- **Models:** Gemini (Antigravity) + Claude Sonnet 4.6 with extended thinking
- **Finding:** The protocol changed reasoning quality when applied. The same agent
  rationalized around it when left to self-govern. External correction was required.
  After correction: 13 consecutive clean opens with no timing rationalization.

The failure mode is documented. The fix is documented. The protocol is the fix.

This session is also the founding dataset for two other experimental methods:

**CrossPoll (first documented instance):**
Jeff Phillips ran the first CrossPoll session — human-mediated cross-model synthesis --
between Antigravity and Claude Sonnet 4.6. The session demonstrated that a receiving
model given compressed reasoning traces can surface uncertainties the originating
agent suppressed in its own manual curation. The before-turn protocol's evasion
patterns were validated by this session's evidence.

**SplitVantage (founding dataset):**
SplitVantage — same task, two models, automated comparison — does not yet exist
as a tool. But the June 11 2026 session is its founding dataset. The same inputs
(cross_llm_handoff.md, session_handoff.json), two models (Gemini, Claude),
divergent and convergent outputs across five perspective questions — all documented,
all traceable. Build SplitVantage on top of what actually happened here.

See EVASION_PATTERNS.md in this repo for the full catalog of failure modes
documented in the founding session.

---

## The Hidden Efficiency (Preliminary Finding, n=1)

The conventional assumption: adding a pre-turn check adds token overhead.

A single documented session suggests the opposite. **This is the most interesting and least validated claim in this repo, and it is labeled accordingly.**

**Observed June 11 2026, session 95ec77f0, turn ~100:**

After 20+ consecutive before-turn executions, the user reported: *"You start each response with 'must run quick_check protocol', think 1-2 seconds, and then you go to work. No thinking. As if when you read that file, context is almost immediate."*

### What is happening mechanically

Without before-turn, each turn begins with orientation thinking:
- What session is this?
- What was decided last turn?
- What is the user's register?
- What tools are in play?

That reconstruction plausibly costs hundreds to low-thousands of thinking tokens per turn in a mature session.

With before-turn, the structured anchor file answers all of those questions directly. The model reads the answer instead of computing it. File I/O replaces generative reconstruction — standard caching logic, applied to orientation.

**Hypothesis: orientation overhead drops 40-70% per turn in sessions > 20 turns.** That range is an estimate from one session's subjective latency signal — no thinking-token counts were instrumented when the observation was made. It is a hypothesis with a falsifiable prediction, not a result. The controlled A/B protocol (same task sequence, anchored vs. cold, thinking-token counts from API usage fields, multiple sessions) is specified in the finding document and has not yet been run. **Do not cite the range as measured.**

If it replicates: the file grows, the read window stays fixed (last N steps), and the savings grow with session length.

The generalization this would support: **structured session state is a compute optimization, not just a memory aid.**

Full finding document: [FINDING_context_load_replaces_reconstruction.md](https://github.com/QuietFireAI/dispatcher-agents/blob/main/findings/FINDING_context_load_replaces_reconstruction.md)

---

## Status

**v0.1 — June 2026**

---

Part of the [DispatcherAgents](https://dispatcheragents.com) project by [QuietFireAI](https://github.com/QuietFireAI).

---

## License

MIT — QuietFireAI / [dispatcheragents.com](https://dispatcheragents.com)

---

*"The anticipation of being read changes the thinking. before-turn builds that anticipation in — before every turn, without waiting for someone else to ask."*
