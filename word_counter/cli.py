"""CLI interface for word_counter project.
"""
import argparse
import time


def count_words(filename):
    """
    Count words in a text file.
    input: filename (str)
    output: word_count (int)
    """
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)


def main():
    parser = argparse.ArgumentParser(description="Count words in a text file")
    parser.add_argument("filename", help="Path to the text file")
    args = parser.parse_args()

    start_time = time.time()
    word_count = count_words(args.filename)
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Word count: {word_count}")
    print(f"Time taken: {execution_time:.6f} seconds")
