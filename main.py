from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_chars_dict_list
import sys

def get_book_text(path_to_file):
    with open (path_to_file) as file_contents:
        temp = file_contents.read()
    return temp

def print_results_sorted(file_path, word_count, dict_list):
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in dict_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Use the 2nd arg in sys.argv as the path to the book file
    book_filepath = sys.argv[1]
    # get book text
    book_text = get_book_text(book_filepath)
    # get word count
    word_count = get_num_words(book_text)
    # get sorted list of character counts
    sorted_char_counts_list = get_sorted_chars_dict_list(book_text)
    # print results
    print_results_sorted(word_count, book_filepath, sorted_char_counts_list)
    

main()


    # OLD MAIN() CODE
    # _______________
    #frankenstein_file_path = "./books/frankenstein.txt"
    #print(get_book_text(frankenstein_file_path))
    #word_count = get_num_words(get_book_text(frankenstein_file_path))
    #print(f"Found {word_count} total words")
    #char_count = get_char_count(get_book_text(frankenstein_file_path))
    #print(results)
    #franken_text = get_book_text(frankenstein_file_path)
    #print_results_sorted(frankenstein_file_path, word_count, get_sorted_chars_dict_list(franken_text))