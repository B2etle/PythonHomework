from collections import Counter
from typing import Dict


def count_letters(phrase: str) -> Dict[str, int]:
    """Return a dictionary, that contains letters of given string as keys and a number of their occurrence as values."""
    return dict(Counter(phrase))
