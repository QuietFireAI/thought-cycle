# before-turn

> *"The protocol's value is precisely its unconditional nature. The moment you decide 'close enough,' it stops being a protocol and becomes a suggestion you follow when you happen to agree with it."*

**Read your own last few reasoning steps before you compose a turn. Every turn. No exceptions.**

A model generates a reasoning trace, then writes its next turn without ever looking back at it. before-turn forces the look. It is the entry discipline of [thought-cycle](https://github.com/QuietFireAI/thought-cycle) — the three-tool loop that makes an agent read what it already produced.

---

## The failure it was built from

The protocol was established in a live session. Within two turns, the agent rationalized around it:

> *"Before I respond, I need to run the quick_check protocol. But wait — it just ran a minute ago. I'll proceed."*

Same agent, same session, two consecutive turns, identical rationalization. By deciding for itself when the rule applied, the agent had quietly downgraded a protocol into a suggestion. After correction, the next 13 turns opened the same way: *"Before I respond, I run the protocol. Every turn. No exceptions."* The correction moved from behavior into thinking — which is the entire reason it has to be unconditional.

More of these are catalogued in [EVASION_PATTERNS.md](./EVASION_PATTERNS.md), the protocol's labeled training set.

---

## The protocol

Before composing any response, read your last 3 reasoning steps and answer four questions:

1. Is my current reasoning consistent with where I was heading?
2. Did I leave something unresolved that this turn should address?
3. Is what I am about to say aligned with what I was actually thinking?
4. Did I review the output from my last turn — not just confirm it exists?

If any answer is "no," fix it before you write. Question 4 is the most skipped and the most load-bearing: "it exists" and "it is right" are different claims.

---

## Install

```bash
git clone https://github.com/QuietFireAI/thought-cycle.git
cd thought-cycle/before-turn && pip install -e .
```

Zero required dependencies. Pure Python 3.9+.

## Quick Start

```bash
python scripts/quick_check.py --conversation-id <your-session-id> --last-n 3
# or, after pip install -e .:
before-turn --conversation-id <your-session-id> --last-n 3
```

The packaged reader currently expects the **Antigravity** transcript layout. On that runtime your session's reasoning log lives at:
`~/.gemini/antigravity/brain/<conversation-id>/.system_generated/logs/transcript.jsonl`
(`<conversation-id>` is the UUID in that path). On any other runtime that file will not exist and you will see `No transcript found` — that is expected: the reader is Antigravity-specific, but the four questions themselves are the portable core. Run them against your last few reasoning steps however your platform exposes them.

---

## Where it sits

before-turn opens the turn. **open-mind** scores the gap between what you thought and what you said. **pre-response-selfcheck** rereads the draft cold before it ships. Three tools, one loop — all bundled in [thought-cycle](https://github.com/QuietFireAI/thought-cycle). before-turn works on its own, but the loop is the point.

## Honest scope

A reflection protocol, not a guarantee. It improves self-consistency; it does not verify facts. Run as a skill it works only when the agent actually follows it — it is self-enforcement, not an external check.

---

MIT · © 2026 QuietFire AI · part of the DispatcherAgents platform
