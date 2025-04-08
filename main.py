import string
from string import ascii_lowercase
from stats import get_num_words
import sys


def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    w_count = get_num_words(text)
    c_count = char_count(text)
    c_count_list = char_dict_to_list(c_count)
    c_count_list.sort(reverse=True, key=sort_character)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")
    for item in c_count_list:
        print(f"{item['character']}: {item['count']}")
    print("============= END ===============")
    

def new_func():
    return type

def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_count(text):
    lowered = text.lower()
    characters = {}
    for i in string.ascii_lowercase:
        characters[i] = lowered.count(i)
    return characters

def sort_character(dict):
    return dict["count"]

def char_dict_to_list(dict):
    lst = []
    for i in ascii_lowercase:
        new_dict = {}
        new_dict["character"] = i
        new_dict["count"] = dict[i]
        lst.append(new_dict)
    return lst


main()