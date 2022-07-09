from __future__ import annotations
from beginnercodes.challenges import test


how_many_missing = lambda x: len([*range(x[0], x[-1] + 1)]) - len(x) if x else 0


test(491, how_many_missing)  # Tell it which challenge to test against
