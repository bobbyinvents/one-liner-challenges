from __future__ import annotations
from beginnercodes.challenges import test


one_odd_one_even = lambda x: (l := [*map(lambda i: int(i) % 2, str(x))])[0] ^ l[1]


test(492, one_odd_one_even)  # Tell it which challenge to test against
