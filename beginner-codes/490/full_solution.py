from __future__ import annotations
from beginnercodes.challenges import test
from time import time


def fill_open_seats(seats: list[int], open_seats: list[int]) -> list[int]:
    if not open_seats:
        return [seats.count(1)]

    new_seats = [i for i in seats]
    new_seats[open_seats[0]] = 1
    new_open_seats = [
        i
        for i in range(len(new_seats))
        if new_seats[i] == 0 and 1 not in new_seats[max(0, i - 2) : i + 3]
    ]

    return fill_open_seats(seats, open_seats[1:]) + fill_open_seats(
        new_seats, new_open_seats
    )


def maximum_seating(seats: list[int]) -> int:
    open_seats = [
        i
        for i in range(len(seats))
        if seats[i] == 0 and 1 not in seats[max(0, i - 2) : i + 3]
    ]
    max_seats = fill_open_seats(seats, open_seats)
    return max(max_seats) - seats.count(1)


test(490, maximum_seating)  # Tell it which challenge to test against
