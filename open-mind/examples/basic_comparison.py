"""
open-mind - quick demonstration

Shows the core comparison in 10 lines.
Reproduce the A/B test from the founding session (June 10-11, 2026).
"""

from open_mind import Comparator

thinking = (
    "I need to be clear about what I actually know versus what I'm "
    "speculating on. The user has observed something real, but I should "
    "resist overinterpreting it."
)

response = (
    "You found something structurally different. Here's what actually "
    "happened: the response is optimized for presentation."
)

result = Comparator.compare(thinking=thinking, response=response)

print(f"Drift score:  {result.drift_score:.2f}")
print(f"Signals:      {len(result.signals)}")
print()
print(result.summary)
print()
print("--- Reflection text (prepend to next turn) ---")
print(result.reflection_text)
