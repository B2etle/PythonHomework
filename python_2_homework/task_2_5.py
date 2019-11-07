from re import sub
from typing import Tuple


def get_digits(num: int) -> Tuple[int]:
    """Returns a tuple of a given integer's digits"""

    return tuple(int(x) for x in str(num))
