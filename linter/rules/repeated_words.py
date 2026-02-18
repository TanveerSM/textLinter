import re


def find_repeated_words(text):
    """
    Finds consecutive repeated words in the text.
    Returns a list of tuples: [(word, start_index, end_index)]
    """
    # Regex explanation:
    # \b(\w+)\b  → captures a word
    # \s+        → one or more spaces
    # \1         → the same word again (backreference)
    pattern = re.compile(r'\b(\w+)\s+\1\b', re.IGNORECASE)
    results = []
    for match in pattern.finditer(text):
        word = match.group(1)
        start = match.start()
        end = match.end()
        results.append((word, start, end))
    return results


