import string
from string import ascii_lowercase


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    w_count = word_count(text)
    c_count = char_count(text)
    c_count_list = char_dict_to_list(c_count)
    c_count_list.sort(reverse=True, key=sort_character)
    print(f"--- Begin report of {book_path} ---")
    print(f"{w_count} word found in the document")
    print("")
    for item in c_count_list:
        print(f"The '{item['character']}' character was found '{item['count']}' times")
    print("--- End report ---")
    

def new_func():
    return type


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

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