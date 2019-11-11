from re import sub


def is_palindrome(phrase: str) -> bool:
    """Check a string is a palindrome or not."""
    phrase = sub(r'[^A-Za-z1-9]', '', phrase.lower())

    return phrase == phrase[::-1]
