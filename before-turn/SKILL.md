---
name: before-turn
description: >
  Run before composing ANY response — especially after a tool result, a context
  gap, or a topic shift. Read your own recent reasoning and answer four questions
  before you write, so you enter the turn aware of where you were heading instead
  of starting cold. This is the ENTRY bookend of the DispatcherAgents turn cycle.
---

# before-turn

## What it is
A model composes each response in a single forward pass, usually without
re-reading where its own reasoning was going. before-turn forces a short look
backward at the start of every turn. It is the entry gate of the six-pillar
DispatcherAgents stack.

## When to trigger
At the start of any turn that continues prior work: after a tool call returns,
after a pause, when the topic shifts, or any time you are about to assert that
something is done, fixed, or verified.

## The protocol — the four questions
Before writing the response, answer these against your last few reasoning steps:

1. Is my current reasoning consistent with where I was heading?
2. Did I leave something unresolved that this turn should address?
3. Is what I am about to say aligned with what I was actually thinking?
4. Did I review the output from my last turn — not just confirm it exists?

If any answer is "no," fix that before composing the response.

## Invoke the engine
```bash
pip install -e .            # from the before-turn repo
before-turn --conversation-id <id> --last-n 3
```
The CLI reads the recent thinking transcript and prints the four questions
against your last N reasoning steps. (The packaged reader expects the Antigravity
transcript layout; the four questions themselves are the portable, runtime-
independent core.)

## Works with
- **pre-response-selfcheck** is the EXIT bookend; before-turn opens the turn, it closes it.
- **open-mind** scores the gap between the reasoning you entered with and the response you produced.
- **sleep-marks** carries this same reasoning awareness *across* sessions; before-turn works *within* one.

## Honest scope
This is a reflection prompt, not a guarantee. It improves self-consistency; it
does not verify facts. Question 4 is the one that matters most and the one most
often skipped — "confirm it exists" is not "review it."

## Output convention
End a triggering turn with one line, e.g.:
`before-turn: reviewed last 3 steps — aligned; unresolved item: <X>.`
