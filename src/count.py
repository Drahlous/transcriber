from collections import Counter
import string
import sys

def count_occurences(filename, word_to_count):
    with open(filename) as f:
        words = f.read()
        # Remove punctuation
        words = words.translate(str.maketrans('', '', string.punctuation))
        # Convert to lowercase
        words = words.lower()
        # Split into words
        words = words.split()
        # Count occurences of each word
        counts = Counter(words)
        print(f"Found {counts[word_to_count]} instances of '{word_to_count}'")

if __name__ == "__main__":
    filename = sys.argv[1]
    WORD_TO_COUNT = sys.argv[2]
    count_occurences(filename, WORD_TO_COUNT)