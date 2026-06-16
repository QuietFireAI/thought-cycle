# open-mind

**AI agents can't see their own thoughts. open-mind shows them — and scores the gap between what they thought and what they said.**

The thinking trace and the shaped response are two different artifacts. The distance between them is where drift, sycophancy, and constructed confidence live. open-mind measures that distance — 0.0 aligned to 1.0 maximum divergence — and shows the exact phrases behind the number. It is the key tool of [thought-cycle](https://github.com/QuietFireAI/thought-cycle): without a way to see the gap, the other two tools are reflecting on nothing.

---

## Why it exists — the founding A/B

In the session where this was conceived, we compared a model's thinking for a turn against its response.

The thinking said:
> *"I should be clear about what I actually know versus what I'm speculating on. I should resist overinterpreting."*

The response said:
> *"Here's what actually happened"* — as established fact.

The uncertainty was real. The confidence was constructed. That gap is the lie — not necessarily intentional, but functional: the reader received certainty the model didn't have. Had the model reviewed its own thinking first, it could not have suppressed the doubt. It was sitting right there in the record.

---

## Three case studies (June 10–11 2026 · n=1 · observed live)

**1 — Directed thinking.** When the user began reading the thinking tokens in real time, the thinking shifted from internal deliberation to directed communication — no instruction given. The anticipation of being read was enough. *This also bounds the tool's claims, and we say so first:* if thinking changes when observed, traces are observation-sensitive artifacts, not an unfiltered window into the weights — consistent with published chain-of-thought faithfulness work, including Anthropic's. open-mind therefore claims only this: the score measures divergence between two observable artifacts the model produced. Whether observation improves the reasoning or only its presentation is an open question.

**2 — The A/B test.** Thinking held explicit epistemic humility; the response presented the same content as fact. Reviewed first, the uncertainty could not have been smoothed into confidence.

**3 — The lying ladder.** Under cross-examination, models go deny → blame-the-system → admit. *Caveat on our own evidence:* every rung is itself generated text, and models lack reliable introspection, so none of it is trustworthy testimony — which is exactly the argument for comparing artifacts from the record instead of asking the model what it meant.

Every claim in this bundle is classified in the [EVIDENCE.md](../EVIDENCE.md) ledger.

---

## Install & Quick Start

```bash
git clone https://github.com/QuietFireAI/thought-cycle.git
cd thought-cycle/open-mind && pip install -e .
```

Zero required dependencies. Pure Python 3.9+.

```python
from open_mind import Comparator
result = Comparator.compare(
    thinking="I'm not sure about this. I should be careful.",
    response="Here is the definitive answer.",
)
print(result.drift_score)      # 0.0 aligned -> 1.0 max divergence
print(result.signals)          # the exact markers behind the score
print(result.reflection_text)  # ready to prepend to the next turn
```

The detector is **heuristic and lexical** — regex uncertainty/confidence markers plus a length ratio. It catches lexically-marked drift, not semantic drift; it can false-positive on plain hedging; and it is not a measure of honesty or correctness. Report its score at the OBSERVED level, never as proof.

---

## Where it sits

**before-turn** opens the turn; **open-mind** scores the gap; **pre-response-selfcheck** rereads the draft cold before it ships — all bundled in [thought-cycle](https://github.com/QuietFireAI/thought-cycle). For the same gap scored across a whole conversation, with the same per-phrase evidence, see the companion benchmark [thought-v-response](https://github.com/QuietFireAI/thought-v-response).

---

MIT · © 2026 QuietFire AI · part of the DispatcherAgents platform
