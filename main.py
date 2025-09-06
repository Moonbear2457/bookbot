from stats import get_num_words, get_num_characters, pretty_report
import sys

if len(sys.argv) != 2:
    raise TypeError("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    print(pretty_report(book_text))