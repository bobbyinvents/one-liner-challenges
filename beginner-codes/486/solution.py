from __future__ import annotations
from beginnercodes.challenges import test
from typing import TypeVar


remove_dups = lambda x: [*dict.fromkeys(x)]


test(486, remove_dups)  # Tell it which challenge to test against
