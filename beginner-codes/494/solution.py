from __future__ import annotations
from beginnercodes.challenges import test


poker_hand_ranking = lambda h: [is_same_suits:=len(set(get_suits:=[c[-1] for c in h]))==1, get_ranks:=[c[:-1] for c in h], is_in_sequence:="".join(sorted(get_ranks,key=({str(i): i for i in range(2, 11)} | {"J": 11, "Q": 12, "K": 13, "A": 14}).get)) in "2345678910JQKA2345" + "2JQKA" + "23QKA" + "234KA" + "2345A", "Royal Flush" if is_same_suits and sorted(get_ranks)==sorted(["A", "K", "Q", "J", "10"]) else "Straight Flush" if is_same_suits and is_in_sequence else "Four of a Kind" if (is_poker_combo := lambda u,c: len(set(get_ranks))==u and get_ranks.count(get_ranks[0]) in c)(2,[1,4]) else "Full House" if is_poker_combo(2, [2,3]) else "Flush" if len(set(get_suits))==1 else "Straight" if not is_same_suits and is_in_sequence else "Three of a Kind" if is_poker_combo(3, [1,3]) else "Two Pair" if is_poker_combo(3, [1,2]) else "Pair" if is_poker_combo(4, [1,2]) else "High Card"][-1]


test(494, poker_hand_ranking)  # Tell it which challenge to test against
