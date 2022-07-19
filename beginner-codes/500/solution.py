from __future__ import annotations
from beginnercodes.challenges import test


maskify = lambda x: "#"*(len(x)-4) + x[-4:]


test(500, maskify)  # Tell it which challenge to test against