from stats import split_book
from stats import num_characters
from stats import char_sort
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    contents = get_book_text(sys.argv[1])

    split_book(contents)
    char_sort(num_characters(contents))


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


main()
