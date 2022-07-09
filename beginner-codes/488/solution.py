from __future__ import annotations
from beginnercodes.challenges import test


can_find = lambda bs, ws: all(any(b in w for w in ws) for b in bs)


test(488, can_find)  # Tell it which challenge to test against
