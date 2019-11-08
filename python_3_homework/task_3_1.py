from collections import Counter
from functools import reduce
from itertools import chain
from string import ascii_lowercase
from typing import List, Set


def test_1_1(*strings: str) -> Set[str]:
    """Return characters that appear in all strings."""
    return sorted(reduce(set.intersection, map(set, strings)))


def test_1_2(*strings: str) -> Set[str]:
    """Return characters that appear in at least one string."""
    return sorted(reduce(set.union, map(set, strings)))


def test_1_3(*strings: str) -> Set[str]:
    """Return characters that appear at least in two strings."""
    # returns dict: keys - unique letters; values - number of letters in words
    ch_number = Counter(chain(*map(list, map(set, strings))))

    return sorted([key for key, value in ch_number.items() if value > 1])


def test_1_4(*strings: str) -> Set[str]:
    """Return characters of alphabet, that were not used in any string."""
    return sorted(reduce(set.difference, [set(ascii_lowercase)] + list(map(set, strings))))
