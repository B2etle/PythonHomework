from typing import List, Tuple


def get_pairs(lst: List) -> List[Tuple]:
    """Returns a list of tuples containing pairs of elements"""

    return [(x,y) for x,y in zip(lst, lst[1:])] if len(lst) > 1 else None
