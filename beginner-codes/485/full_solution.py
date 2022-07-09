from __future__ import annotations
from beginnercodes.challenges import test


def filter_words(words: list[str], mask: str) -> list[str]:
    filtered = []
    for w in words:
        mismatch = False
        if len(w) != len(mask):
            continue
        for i in range(min(len(w), len(mask))):
            if mask[i] == "*" or w[i] == mask[i]:
                continue
            else:
                mismatch = True
        if not mismatch:
            filtered.append(w)

    return filtered


test(485, filter_words)  # Tell it which challenge to test against
