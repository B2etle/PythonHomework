from re import sub
from typing import List


def split_phrase(phrase: str, separator: str = ' ', maxsplit: int = -1) -> List[str]:
    """Splits string by a separator"""
    
    indexes = [x for x, ch in enumerate(phrase) if ch == separator][:maxsplit if maxsplit > -1 else None]

    return [phrase[x+1:y] for x, y in zip([-1] + indexes, indexes + [len(phrase)])]
