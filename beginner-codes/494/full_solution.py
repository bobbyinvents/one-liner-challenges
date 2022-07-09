from __future__ import annotations
from beginnercodes.challenges import test

number_card_value_dict = {str(i): i for i in range(2, 11)}
face_card_value_dict = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}
card_value_dict = number_card_value_dict | face_card_value_dict


def get_ranks(hand: list[str]) -> list[str]:
    return [card[:-1] for card in hand]


def get_suits(hand: list[str]) -> list[str]:
    return [card[-1] for card in hand]


def is_same_suits(hand: list[str]) -> bool:
    return len(set(get_suits(hand))) == 1


def compare_ranks(hand: list[str], values: list[str]) -> bool:
    return sorted(get_ranks(hand)) == sorted(values)


def order_hand(hand: list[str]) -> list[str]:
    return sorted(get_ranks(hand), key=card_value_dict.get)


def is_in_sequence(hand: list[str]) -> bool:
    return (
        "".join(order_hand(hand))
        in "2345678910JQKA2345" + "2JQKA" + "23QKA" + "234KA" + "2345A"
    )


assert is_in_sequence(["10h", "Js", "Qd", "Kd", "Ac"]) is True
assert is_in_sequence(["Jh", "Qs", "Kd", "Ad", "2c"]) is True
assert is_in_sequence(["Ah", "2s", "3d", "4d", "5c"]) is True


def is_poker_combo(hand: list[str], unique_cards: int, card_counts: list[int]) -> bool:
    ranks = get_ranks(hand)
    return len(set(ranks)) == unique_cards and ranks.count(ranks[0]) in card_counts


def royal_flush(hand: list[str]) -> bool:
    return is_same_suits(hand) and compare_ranks(hand, ["A", "K", "Q", "J", "10"])


assert royal_flush(["10h", "Jh", "Qh", "Ah", "Kh"]) is True
assert royal_flush(["10h", "10h", "Qh", "Ah", "Kh"]) is False
assert royal_flush(["10h", "10h", "10h", "10h", "10h"]) is False
assert royal_flush(["10h", "Jh", "Qh", "Ah", "Kc"]) is False


def straight_flush(hand: list[str]) -> bool:
    return is_same_suits(hand) and is_in_sequence(hand)


def four_of_a_kind(hand: list[str]) -> bool:
    return is_poker_combo(hand, 2, [1, 4])


assert four_of_a_kind(["Jc", "Jh", "Jd", "Js", "Kh"]) is True
assert four_of_a_kind(["Jc", "Jh", "Jd", "Ks", "Kh"]) is False


def full_house(hand: list[str]) -> bool:
    return is_poker_combo(hand, 2, [2, 3])


assert full_house(["Jc", "Jd", "Jh", "Kh", "Ks"]) is True
assert full_house(["Jc", "Jd", "As", "Kh", "Ks"]) is False
assert full_house(["Jc", "Jd", "Js", "Jh", "Ks"]) is False


def flush(hand: list[str]) -> bool:
    return len(set(get_suits(hand))) == 1


def straight(hand: list[str]) -> bool:
    return not is_same_suits(hand) and is_in_sequence(hand)


def three_of_a_kind(hand: list[str]) -> bool:
    return is_poker_combo(hand, 3, [1, 3])


def two_pair(hand: list[str]) -> bool:
    return is_poker_combo(hand, 3, [1, 2])


def pair(hand: list[str]) -> bool:
    return is_poker_combo(hand, 4, [1, 2])


assert pair(["Kh", "Kh", "2h", "3d", "4s"]) is True


def poker_hand_ranking(hand: list[str]) -> str:
    if royal_flush(hand):
        return "Royal Flush"
    elif straight_flush(hand):
        return "Straight Flush"
    elif four_of_a_kind(hand):
        return "Four of a Kind"
    elif full_house(hand):
        return "Full House"
    elif flush(hand):
        return "Flush"
    elif straight(hand):
        return "Straight"
    elif three_of_a_kind(hand):
        return "Three of a Kind"
    elif two_pair(hand):
        return "Two Pair"
    elif pair(hand):
        return "Pair"

    return "High Card"


test(494, poker_hand_ranking)  # Tell it which challenge to test against
