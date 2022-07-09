from __future__ import annotations
from beginnercodes.challenges import test
from typing import TypeVar


matrix = lambda x, y, z: [[z for j in range(y)] for i in range(x)]


test(487, matrix)  # Tell it which challenge to test against
