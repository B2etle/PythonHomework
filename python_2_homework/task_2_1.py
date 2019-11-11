def replace_quotes(phrase: str) -> str:
    """Replace all " symbols with ' and vise versa."""
    return phrase.translate(phrase.maketrans({'\'': '\"', '\"': '\''}))
