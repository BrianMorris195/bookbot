import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def sort_num(dict):
        return dict["num"]

from stats import get_num_words
from stats import get_num_char
from stats import char_count_list

def main():
        if len(sys.argv) < 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words = get_num_words(text)
        char = get_num_char(text)
        report_counts = char_count_list(char)
        report_counts.sort(reverse=True, key=sort_num)
        print_report(filepath, num_words, report_counts)

    

def print_report(filepath, num_words, report_counts):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in report_counts:
                if not item["char"].isalpha():
                        continue   
                print(f"{item['char']}: {item['num']}")

        print("============= END ===============")
        

      



main()