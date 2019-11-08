from typing import Dict


def generate_squares(snum: int) -> Dict[int, int]:
    """Return a dictionary, where the key is a number and the value is the square of that number."""
    return {num: num ** 2 for num in range(1, snum + 1)}
