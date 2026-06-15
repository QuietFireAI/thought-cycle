# thought-cycle

**Agents have thoughts. They just never read them.**

A model generates a reasoning trace on every turn — and then ignores it. It
doesn't check what it said against what it thought. `thought-cycle` is three
small skills that close that loop. They don't give a model new abilities; they
make it *read what it already produced*. It was inside the whole time — this just
looks.

Part of the **DispatcherAgents** platform.

---

## The cycle (open-mind is the key)

Everything turns on **open-mind**. Without a way to see the gap between what was
thought and what was said, the other two are blind — reflection with nothing to
reflect on, a final check with no signal. So read it in this order:

1. **open-mind** — *the access point.* Compares the thinking trace against the
   shaped response and scores the drift: suppressed uncertainty, constructed
   confidence, over-compression. This is the eye. Start here.
2. **before-turn** — *reflection at entry.* Before composing a turn, read your
   own recent reasoning and answer four questions, so you don't start cold.
3. **pre-response-selfcheck** — *the exit gate.* Before sending, reread the draft
   as a cold reader and either pass it or fix one line.

before-turn opens the turn, open-mind reads the gap, pre-response-selfcheck
closes it. One loop.

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

---

## What this is — and is not

- **It surfaces, it does not add.** These tools expose reasoning the model already
  generated. They grant no new capability and make no claim to.
- **Self-enforcement when followed.** Run as skills, they work by the agent
  actually following them. They are not an unfakeable hook on generation. The hard
  guarantee is an *external* observer — that's the rest of the DispatcherAgents
  platform, released as it's ready.
- **Heuristic, not omniscient.** open-mind's drift detector is lexical (see its
  own README). It catches marked drift, not all drift, and it is not a measure of
  honesty or correctness.

---

## Coming next in the platform

`agent-open-mind` · `sleep-marks` · `splitvantage` — in polish, released in order.

## Contact & license

Questions, issues, disclosure: **support@quietfireai.com**.
MIT. © 2026 QuietFire AI.
