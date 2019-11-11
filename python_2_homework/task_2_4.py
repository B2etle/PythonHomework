from re import sub
from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """Split the 's' string by indexes specified in 'indexes'."""
    return [s[x:y] for x, y in zip([0] + indexes, indexes + [len(s)]) if y > x]
