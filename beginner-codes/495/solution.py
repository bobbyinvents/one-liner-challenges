from __future__ import annotations
from beginnercodes.challenges import test


number_split = lambda x: [[a := x // 2] * 2, sorted([a, a + 1])][x % 2]

test(495, number_split)  # Tell it which challenge to test against
