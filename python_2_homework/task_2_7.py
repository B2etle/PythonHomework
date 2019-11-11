from functools import reduce
from typing import List

from numpy import multiply


def foo(lnum: List[int]) -> List[int]:
    """Given a list of integers, return a new list.

    In that list each element at index 'i' of the new list is the product of all
    the numbers in the original array except the one at 'i'.
    """
    numval = reduce(multiply, lnum)

    return [int(numval/x) for x in lnum]
