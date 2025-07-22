from stats import sorted_report
from stats import  word_count
import sys

def main():
    words_dictionary = word_count()
    report_sorted = sorted_report()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f"Found {words_dictionary} total words")
    print("--------- Character Count -------")
    for letter, count in report_sorted:
        print(f"{letter}: {count}")
    print("============= END ===============")

print("Usage: python3 main.py <path_to_book>")
main()