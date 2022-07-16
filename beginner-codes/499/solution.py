from __future__ import annotations
from beginnercodes.challenges import test


overlap = lambda a, b: a + b[([0]+[i for i in range(len(a)+1) if a[-i:]==b[:i]])[-1]:]


test(499, overlap)  # Tell it which challenge to test against