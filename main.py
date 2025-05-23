import sys

from stats import get_num_words, count_characters, sort_on_num, sort_num

if len(sys.argv) !=2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    word_count = get_num_words(text)

    print("--------- Character Count -------")

    char_counts = count_characters(text)

    sorted_char_list = sort_num(char_counts)

    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()