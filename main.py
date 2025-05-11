def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(file_contents):
    text = file_contents.split()
    return len(text)


def main():
        filepath = "books/frankenstein.txt"
        file_contents = get_book_text(filepath)
        num_words = get_num_words(file_contents)

        print(f"{num_words} words found in the document")
      

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