import string
import sys

def get_book_text():
    path = sys.argv[1]
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def word_count():
    book_data = get_book_text()
    book_data_split = book_data.split()
    book_data_count = len(book_data_split)
    return book_data_count

def letter_count():
    list_count_numbers = []
    book_data = get_book_text()
    book_data_lower = book_data.lower()
    book_data_split = list(book_data_lower)
    alphabeth = list(string.ascii_lowercase)
    for letter in alphabeth:
        if letter in book_data_split:
            letter_counter = book_data_split.count(letter)
            list_count_numbers.append(letter_counter)
        else:
            list_count_numbers.append(letter_counter)
    
    dictionary = dict(zip(alphabeth, list_count_numbers))
    return dictionary

def key_getter(items):
    return items[1]

def sorted_report():
    obtain = letter_count()
    obtain_count = obtain.items()
    sorted_items = sorted(obtain_count,key=key_getter, reverse=True)
    return sorted_items
        