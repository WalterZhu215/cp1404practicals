"""
Word Occurrences
Estimate time: 25 minutes
Actual time: 30 minutes

This program counts the occurrences of each word in a user-provided string.
It displays the results sorted alphabetically and aligned in columns.
"""


def main():
    """Count word occurrences and display formatted results."""
    text = input("Text: ").strip()
    word_counts = count_word_occurrences(text)
    display_word_counts(word_counts)


def count_word_occurrences(text):
    """Count occurrences of each word in the given text."""
    words = text.split()
    word_counts = {}

    for word in words:
        word = word.lower()  # Make case-insensitive
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def display_word_counts(word_counts):
    """Display word counts sorted alphabetically with aligned output."""
    sorted_words = sorted(word_counts.keys())
    longest_word_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        print(f"{word:{longest_word_length}} : {word_counts[word]}")


main()
