def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_num_char
from stats import char_count_list

def main():
        filepath = "books/frankenstein.txt"
        text = get_book_text(filepath)
        num_words = get_num_words(text)
        char = get_num_char(text)
        report_counts = char_count_list(char)

        print(f"{num_words} words found in the document")
        print(char)
        print(char_count_list)

      

"""
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)
"""
main()