from __future__ import annotations
from beginnercodes.challenges import test


little_big = lambda n: n//2+5 if n%2 else 100*2**(n/2-1)


test(497, little_big)  # Tell it which challenge to test against