from __future__ import annotations
from beginnercodes.challenges import test


filter_words = lambda ws, m: list(filter(lambda w: len(w)==len(m) and all(m[i] == "*" or w[i] == m[i] for i in range(min(len(w), len(m)))), ws))


test(485, filter_words)  # Tell it which challenge to test against
