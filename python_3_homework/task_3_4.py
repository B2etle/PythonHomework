from collections import Counter
from functools import reduce
from typing import Dict

from numpy import add


def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    """Return receives changeable number of dictionaries.

    Where keys - letters, values - numbers) and combines them into one dictionary.
    """
    return dict(reduce(add, map(Counter, args)))
