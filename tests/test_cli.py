import unittest
import os
from word_counter.cli import (
    count_words,
)  # Replace 'your_script_name' with your actual script name


class TestCountWords(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file with known content
        self.test_file = "test_file.txt"
        with open(self.test_file, "w") as file:
            file.write("This is a sample sentence.")

    def tearDown(self):
        # Remove the temporary test file
        os.remove(self.test_file)

    def test_count_words(self):
        # Test if the function correctly counts words in a file
        word_count = count_words(self.test_file)
        self.assertEqual(
            word_count, 5
        )  # Expecting 5 words in the test sentence

    def test_empty_file(self):
        # Test when the input file is empty
        empty_file = "empty_file.txt"
        with open(empty_file, "w") as file:
            pass  # Create an empty file
        word_count = count_words(empty_file)
        self.assertEqual(word_count, 0)  # Expecting 0 words in an empty file

    def test_nonexistent_file(self):
        # Test when the input file does not exist
        nonexistent_file = "nonexistent_file.txt"
        with self.assertRaises(FileNotFoundError):
            count_words(nonexistent_file)  # Expecting a FileNotFoundError


if __name__ == "__main__":
    unittest.main()
