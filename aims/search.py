"""Search helpers; return matches without modifying the input."""


def search_by_category(items, category):
    """Match a complete category ignoring case; preserve input order."""
    return [dvd for dvd in items if category.lower() == dvd.category.lower()]


def search_by_title(items, keyword):
    """Return DVDs whose title contains keyword, preserving order."""
    return [dvd for dvd in items if keyword in dvd.title]
