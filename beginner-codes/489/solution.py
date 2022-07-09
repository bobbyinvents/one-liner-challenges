from __future__ import annotations
from beginnercodes.challenges import test


diamond_arrays = lambda s: [[i]*i for i in [*range(1, s+1)]+[*range(s-1, 0, -1)]]


test(489, diamond_arrays)  # Tell it which challenge to test against