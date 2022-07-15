from __future__ import annotations
from beginnercodes.challenges import test


three_letter_collection = lambda x: sorted(x[i:i+3] for i in range(len(x)-2))


test(498, three_letter_collection)  # Tell it which challenge to test against