def get_shortest_word(s: str) -> str:
    """Return the shortest word in the given string."""
    return min(s.split(), key=len)
