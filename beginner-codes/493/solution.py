from __future__ import annotations
from beginnercodes.challenges import test


# Solution 1
remix = lambda s, i: "".join(dict(zip(i, s))[k] for k in range(len(s)))

# Solution 2
remix = lambda s, i: "".join(dict(sorted(zip(i, s))).values())


test(493, remix)  # Tell it which challenge to test against
