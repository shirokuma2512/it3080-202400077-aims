"""Search helpers; return matches without modifying the input."""


def search_by_title(items, keyword):
    """Return DVDs whose title contains keyword, preserving order."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
