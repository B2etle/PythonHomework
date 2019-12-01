from collections import Counter
from typing import List


def most_common_words(filepath: str, number_of_words: int = 3) -> List[str]:
    """Search for most common words in the file."""
    with open(filepath, 'r') as file_text:
        words_number = Counter([word.strip(',.') for word in file_text.read().lower().split()])
        return [word for word, number in words_number.most_common(number_of_words)]
