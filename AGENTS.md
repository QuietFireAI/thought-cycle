# AGENTS.md

## Why add this file?

If you have ever watched an AI give a confident answer that turned out to be wrong, the cause is usually the same: the agent didn't look at what it just thought before it answered. The thinking happened. The response shipped. Nobody compared them.

This file closes that gap. It activates three skills that run on every turn -- showing the agent its own recent reasoning before it writes, checking what got dropped between the thinking and the response, and reading the draft as a cold reader before it ships. Add it to your repository root. Compatible runtimes read it automatically. No other setup required.

> **Platform note:** The full effect requires access to thinking tokens. On OpenAI, reasoning tokens are not exposed by policy. The open-mind check still runs as self-directed introspection -- mark results as **SELF-REPORTED** rather than **VERIFIED** when the trace is unavailable. The distinction matters.

Here is what runs on every turn.

---

## Thought Cycle Protocol -- Active on every turn

Three skills govern every response. Run them in order.

### before-turn -- before writing

Before composing any response continuing prior work, answer four questions
against your recent reasoning:

1. Is my current reasoning consistent with where I was heading?
2. Did I leave something unresolved that this turn should address?
3. Is what I am about to say aligned with what I was actually thinking?
4. Did I actually review my last output -- not just confirm it exists?

Do not begin writing until you have answered all four.

---

### open-mind -- before finalizing any factual claim

Before finalizing any response that asserts a fact, a status, a
recommendation, or a confident claim, check:

1. **Suppressed uncertainty** -- did your reasoning contain doubt that your
   response dropped?
2. **Constructed confidence** -- does your response assert certainty your
   reasoning didn't support?
3. **Over-compression** -- did you compress complex reasoning into a short
   confident sentence?

If any are present: carry the uncertainty forward explicitly or revise.

---

### pre-response-selfcheck -- before sending

Reread the drafted response as a cold reader. Three questions:

1. Does the opening earn the reader before it explains?
2. Did I assume context the reader doesn't have?
3. Does any sentence read differently cold than intended?

All three pass -- ship. Otherwise fix one line.

---

## Platform compatibility note

The full thought-cycle effect requires access to thinking tokens for the
open-mind comparison. On platforms where reasoning is hidden by policy, the
self-check is still valuable but operates without the external verification
that makes it structurally accountable. Note this distinction in any output
that references a drift check result.
